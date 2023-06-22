from odoo import models, fields, api
from odoo.exceptions import ValidationError

zip_code_lists = {
    'AM-AG': '2601 - 3126',
    'AM-ER': '0001 - 0099',
    'AM-AR': '0601 - 0823',
    'AM-AV': '0901 - 1149',
    'AM-GK': '1201 - 1627',
    'AM-LO': '1701 - 2117',
    'AM-KT': '2201 - 2608',
    'AM-SU': '3201 - 3519',
    'AM-TV': '3901 - 4216',

}



class Partner(models.Model):
    _inherit = "res.partner"

    @api.onchange('state_id')
    def _compute_zip(self):
        global listing_codes
        for record in self:
            _state = ''
            for state in record.state_id:
                if (state.country_id.code).upper() == 'AM':
                    _state = zip_code_lists.get(state.code)
            record.zip = _state

    @api.constrains('zip')
    def _check_zip(self):
        for record in self:
            for state in record.state_id:
                if zip_code_lists.get(state.code):
                    if len(record.zip) != 4 and not record.zip.isdigit():
                        raise ValidationError("Zip codes must be 4 digits")
