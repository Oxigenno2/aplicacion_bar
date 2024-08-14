"""add codigo_mesa

Revision ID: 82f7d16d2e04
Revises: 108a478c51b2
Create Date: 2024-08-13 23:19:39.107665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82f7d16d2e04'
down_revision = '108a478c51b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('codigo_mesa', sa.Integer(), nullable=True))
        batch_op.drop_column('table_number')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('codigo_mesa', sa.Integer(), nullable=False))
        batch_op.drop_column('table_number')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('table_number', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_column('codigo_mesa')

    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('table_number', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_column('codigo_mesa')

    # ### end Alembic commands ###