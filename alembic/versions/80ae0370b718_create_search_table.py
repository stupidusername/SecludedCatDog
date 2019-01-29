"""
Create search table.

Revision ID: 80ae0370b718
Revises:
Create Date: 2019-01-29 04:29:23.416790
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils.types.json import JSONType


# Revision identifiers, used by Alembic.
revision = '80ae0370b718'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'search',
        sa.Column('param', sa.String(), primary_key=True),
        sa.Column('create_datetime', sa.DateTime(), nullable=False),
        sa.Column('identity', JSONType, nullable=False)
    )


def downgrade():
    op.drop_table('search')
