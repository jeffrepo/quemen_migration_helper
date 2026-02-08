# -*- coding: utf-8 -*-
from odoo.upgrade import util

def migrate(cr, version):
    util.recompute_fields(cr, "pos.order", [
        "l10n_mx_edi_cfdi_attachment_id",
        "l10n_mx_edi_cfdi_state",
        "l10n_mx_edi_cfdi_sat_state",
        "l10n_mx_edi_cfdi_uuid",
        "l10n_mx_edi_is_cfdi_needed",
        "l10n_mx_edi_cfdi_to_public",
        "l10n_mx_edi_usage",
        "config_id",
    ])