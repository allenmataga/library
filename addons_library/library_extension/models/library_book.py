from odoo import fields, models

class LibraryBook(models.Model):
    _inherit = "library.book"

    author_id = fields.Many2one("res.partner", string="Author", required=True)

    # from my previous work, if it's many2many field the field name must be ids
    category_ids = fields.Many2many( "library.book.category", string="Category")