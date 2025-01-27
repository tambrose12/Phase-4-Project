"""changed race legnth to track_length

Revision ID: 796384866b32
Revises: c09060a35233
Create Date: 2023-04-20 15:32:03.566003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '796384866b32'
down_revision = 'c09060a35233'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('races', schema=None) as batch_op:
        batch_op.add_column(sa.Column('track_length', sa.Float(), nullable=True))
        batch_op.drop_column('length')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('races', schema=None) as batch_op:
        batch_op.add_column(sa.Column('length', sa.FLOAT(), nullable=True))
        batch_op.drop_column('track_length')

    # ### end Alembic commands ###
