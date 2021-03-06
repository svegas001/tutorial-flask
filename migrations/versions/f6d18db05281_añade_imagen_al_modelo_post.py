"""añade imagen al modelo post

Revision ID: f6d18db05281
Revises: 2bf8ce8c32c9
Create Date: 2020-02-03 10:41:37.457599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6d18db05281'
down_revision = '2bf8ce8c32c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('image_name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'image_name')
    # ### end Alembic commands ###
