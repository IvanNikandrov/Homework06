"""Initial

Revision ID: 115b3a5a3620
Revises: 
Create Date: 2022-07-06 15:48:23.858136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '115b3a5a3620'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
