"""chenged DB to postgresql

Revision ID: f1d8e43c229c
Revises: 3bc7da0e3ff9
Create Date: 2024-01-22 09:17:52.487725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1d8e43c229c'
down_revision: Union[str, None] = '3bc7da0e3ff9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
