"""empty message

Revision ID: 380878db06c2
Revises: 
Create Date: 2020-03-13 02:28:42.614472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '380878db06c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('user_name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
