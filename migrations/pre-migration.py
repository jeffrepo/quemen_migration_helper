from odoo.upgrade import util

def migrate(cr, version):

    # sms.sms: evitar operaciones costosas en tablas grandes
    util.alter_column_type(cr, "sms_sms", "uuid", "varchar")
    util.create_column(cr, "sms_sms", "to_delete", "bool", default=False)
    util.create_column(cr, "pos_order", "l10n_mx_edi_cfdi_attachment_id", "int4")
    util.create_column(cr, "pos_order", "l10n_mx_edi_cfdi_state", "varchar")
    util.create_column(cr, "pos_order", "l10n_mx_edi_cfdi_sat_state", "varchar")
    util.create_column(cr, "pos_order", "l10n_mx_edi_cfdi_uuid", "varchar")
    util.create_column(cr, "pos_order", "l10n_mx_edi_is_cfdi_needed", "bool")
    util.create_column(cr, "pos_order", "l10n_mx_edi_cfdi_to_public", "bool")
    util.create_column(cr, "pos_order", "l10n_mx_edi_usage", "varchar", default="'G03'")
