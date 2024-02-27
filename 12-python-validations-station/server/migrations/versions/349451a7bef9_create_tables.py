"""create tables

Revision ID: 349451a7bef9
Revises: 
Create Date: 2024-02-27 13:51:04.614806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '349451a7bef9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('city', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_stations'))
    )
    op.create_table('trains',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('train_num', sa.String(), nullable=True),
    sa.Column('service_type', sa.String(), nullable=True),
    sa.Column('origin', sa.String(), nullable=True),
    sa.Column('destination', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_trains'))
    )
    op.create_table('platforms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('platform_num', sa.Integer(), nullable=True),
    sa.Column('station_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['station_id'], ['stations.id'], name=op.f('fk_platforms_station_id_stations')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_platforms')),
    sa.UniqueConstraint('platform_num', 'station_id', name='unique_platform_per_station')
    )
    op.create_table('assignments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('arrival_time', sa.DateTime(), nullable=True),
    sa.Column('departure_time', sa.DateTime(), nullable=True),
    sa.Column('train_id', sa.Integer(), nullable=True),
    sa.Column('platform_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['platform_id'], ['platforms.id'], name=op.f('fk_assignments_platform_id_platforms')),
    sa.ForeignKeyConstraint(['train_id'], ['trains.id'], name=op.f('fk_assignments_train_id_trains')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_assignments'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assignments')
    op.drop_table('platforms')
    op.drop_table('trains')
    op.drop_table('stations')
    # ### end Alembic commands ###