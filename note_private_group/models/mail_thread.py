# Copyright 2020 Xtendoo Corporation
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, exceptions, fields, models


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    _description = 'Email Thread'

    message_ids = fields.One2many(
        'mail.message',
        'res_id',
        string='Messages',
        domain=lambda self: self._domain_message(),
    )

    @api.model
    def _domain_message(self):
        if self.env.user.has_group('note_private_group.specialist_group'):
            return [('message_type', '!=', 'user_notification')]
        return [('message_type', '!=', 'user_notification'), ('is_private', '=', False)]


