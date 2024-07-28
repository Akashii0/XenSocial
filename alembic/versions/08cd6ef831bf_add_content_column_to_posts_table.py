"""add content column to posts table

Revision ID: 08cd6ef831bf
Revises: a22817cd1c59
Create Date: 2024-07-28 09:57:54.163386

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08cd6ef831bf'
down_revision: Union[str, None] = 'a22817cd1c59'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

