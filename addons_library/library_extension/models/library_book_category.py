from odoo import fields, models

class LibraryBookCategory(models.Model):
    _name = "library.book.category"

    name = fields.Char(string="Name", required=True)


    _sql_constraints = [
        ("make_the_category_unique",
         "unique(name)",
         "You must enter a unique category, Beh!",
        ),
    ]
    