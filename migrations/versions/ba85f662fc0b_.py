"""empty message

Revision ID: ba85f662fc0b
Revises: aa3ccf8d2263
Create Date: 2023-08-13 20:36:18.825362

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ba85f662fc0b'
down_revision = 'aa3ccf8d2263'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('categories',
               existing_type=postgresql.JSONB(astext_type=sa.Text()),
               type_=sa.String(length=64),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('categories',
               existing_type=sa.String(length=64),
               type_=postgresql.JSONB(astext_type=sa.Text()),
               existing_nullable=True)

    # ### end Alembic commands ###
