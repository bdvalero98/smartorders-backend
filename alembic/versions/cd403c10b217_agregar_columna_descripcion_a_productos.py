"""agregar columna descripcion a productos

Revision ID: cd403c10b217
Revises: aaa5ee64f7a7
Create Date: 2025-06-14 18:57:04.677234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd403c10b217'
down_revision: Union[str, None] = 'aaa5ee64f7a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('productos', sa.Column('descripcion', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('productos', 'descripcion')
    # ### end Alembic commands ###
