# Copyright 2020 Xtendoo Corporation
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, exceptions, fields, models


class Message(models.Model):
    _inherit = 'mail.message'

    is_private = fields.Boolean(
        'Message private',
        compute='_get_private',
        store=True,
    )

    @api.depends('author_id')
    def _get_private(self):
        for message in self:
            if message.author_id:
                user = self.env['res.users'].search([('partner_id.id', '=', message.author_id[0].id)])
                if user:
                    message.is_private = user.has_group('note_private_group.private_note_group')
                else:
                    message.is_private = False
            else:
                message.is_private = False
