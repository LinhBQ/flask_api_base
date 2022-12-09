"""empty message

Revision ID: c8c76c417efa
Revises: 7c49759abaca
Create Date: 2022-12-09 14:46:23.651817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8c76c417efa'
down_revision = '7c49759abaca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('age', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'age')
    # ### end Alembic commands ###