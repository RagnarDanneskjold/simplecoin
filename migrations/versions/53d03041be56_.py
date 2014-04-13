"""Adds thresholds and events for tracking email send rates.

Revision ID: 53d03041be56
Revises: 19df16914a19
Create Date: 2014-03-17 22:09:03.802725

"""

# revision identifiers, used by Alembic.
revision = '53d03041be56'
down_revision = '19df16914a19'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('threshold',
                    sa.Column('user', sa.String(), nullable=False),
                    sa.Column('worker', sa.String(), nullable=False),
                    sa.Column('temp_thresh', sa.Integer(), nullable=True),
                    sa.Column('offline_thresh', sa.Integer(), nullable=True),
                    sa.Column('hashrate_thresh', sa.Integer(), nullable=True),
                    sa.Column('hashrate_err', sa.Boolean(), nullable=True),
                    sa.Column('temp_err', sa.Boolean(), nullable=True),
                    sa.Column('offline_err', sa.Boolean(), nullable=True),
                    sa.Column('green_notif', sa.Boolean(), nullable=True),
                    sa.Column('emails', postgresql.ARRAY(sa.String()), nullable=True),
                    sa.PrimaryKeyConstraint('user', 'worker')
                    )
    op.create_table('event',
                    sa.Column('time', sa.DateTime(), nullable=False),
                    sa.Column('user', sa.String(), nullable=False),
                    sa.Column('worker', sa.String(), nullable=False),
                    sa.Column('address', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('time', 'user', 'worker', 'address')
                    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event')
    op.drop_table('threshold')
    ### end Alembic commands ###
