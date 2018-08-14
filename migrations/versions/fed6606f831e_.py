"""empty message

Revision ID: fed6606f831e
Revises: 
Create Date: 2018-08-13 21:38:31.797585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fed6606f831e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=140), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('entries')
    # ### end Alembic commands ###
