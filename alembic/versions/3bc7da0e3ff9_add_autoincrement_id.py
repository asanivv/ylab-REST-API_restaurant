"""add autoincrement ID

Revision ID: 3bc7da0e3ff9
Revises: e5ed9026b9f8
Create Date: 2024-01-21 17:08:48.388367

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3bc7da0e3ff9'
down_revision: Union[str, None] = 'e5ed9026b9f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
