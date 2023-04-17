"""created tables

Revision ID: ffd885953fcb
Revises: 
Create Date: 2023-04-17 11:53:11.852166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffd885953fcb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drivers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('car_number', sa.Integer(), nullable=True),
    sa.Column('team', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('races',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('fastest_time', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('driver_races',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('driver_id', sa.Integer(), nullable=True),
    sa.Column('race_id', sa.Integer(), nullable=True),
    sa.Column('time', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['driver_id'], ['drivers.id'], name=op.f('fk_driver_races_driver_id_drivers')),
    sa.ForeignKeyConstraint(['race_id'], ['races.id'], name=op.f('fk_driver_races_race_id_races')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('driver_races')
    op.drop_table('races')
    op.drop_table('drivers')
    # ### end Alembic commands ###