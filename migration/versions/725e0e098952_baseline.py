"""baseline

Revision ID: 725e0e098952
Revises: 
Create Date: 2021-12-30 10:02:21.517719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '725e0e098952'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blockchain_detail',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('chain_id', sa.VARCHAR(length=50), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('symbol', sa.VARCHAR(length=30), nullable=False),
    sa.Column('logo', sa.VARCHAR(length=250), nullable=False),
    sa.Column('block_confirmation', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('chain_id', 'name', 'symbol')
    )
    op.create_table('token_detail',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('description', sa.VARCHAR(length=250), nullable=False),
    sa.Column('symbol', sa.VARCHAR(length=30), nullable=False),
    sa.Column('logo', sa.VARCHAR(length=250), nullable=True),
    sa.Column('blockchain_id', sa.INTEGER(), nullable=False),
    sa.Column('allowed_decimal', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['blockchain_id'], ['blockchain_detail.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('blockchain_id', 'symbol')
    )
    op.create_table('conversion_fee',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('id', sa.VARCHAR(length=250), nullable=False),
    sa.Column('percentage_from_source', sa.DECIMAL(), nullable=True),
    sa.Column('amount', sa.DECIMAL(), nullable=True),
    sa.Column('token_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['token_id'], ['token_detail.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('token_pair',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('from_token_id', sa.INTEGER(), nullable=False),
    sa.Column('to_token_id', sa.INTEGER(), nullable=False),
    sa.Column('conversion_fee_id', sa.VARCHAR(length=250), nullable=True),
    sa.Column('is_enabled', sa.BOOLEAN(), nullable=True),
    sa.Column('min_value', sa.DECIMAL(), nullable=True),
    sa.Column('max_value', sa.DECIMAL(), nullable=True),
    sa.Column('contract_address', sa.VARCHAR(length=250), nullable=True),
    sa.Column('receiving_address', sa.VARCHAR(length=250), nullable=True),
    sa.ForeignKeyConstraint(['conversion_fee_id'], ['conversion_fee.id'], ),
    sa.ForeignKeyConstraint(['from_token_id'], ['token_detail.id'], ),
    sa.ForeignKeyConstraint(['to_token_id'], ['token_detail.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('from_token_id', 'to_token_id')
    )
    op.create_table('wallet_payer',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('id', sa.VARCHAR(length=250), nullable=False),
    sa.Column('token_pair_id', sa.INTEGER(), nullable=False),
    sa.Column('from_address', sa.VARCHAR(length=250), nullable=False),
    sa.Column('to_address', sa.VARCHAR(length=250), nullable=True),
    sa.ForeignKeyConstraint(['token_pair_id'], ['token_pair.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('conversion',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('id', sa.VARCHAR(length=250), nullable=False),
    sa.Column('wallet_payer_id', sa.VARCHAR(length=250), nullable=False),
    sa.Column('amount', sa.DECIMAL(), nullable=True),
    sa.Column('status', sa.VARCHAR(length=30), nullable=False),
    sa.ForeignKeyConstraint(['wallet_payer_id'], ['wallet_payer.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('transaction',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('id', sa.VARCHAR(length=250), nullable=False),
    sa.Column('conversion_id', sa.VARCHAR(length=250), nullable=False),
    sa.Column('status', sa.VARCHAR(length=30), nullable=False),
    sa.Column('from_transaction_hash', sa.VARCHAR(length=250), nullable=True),
    sa.Column('from_status', sa.VARCHAR(length=30), nullable=True),
    sa.Column('from_updated_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('to_transaction_hash', sa.VARCHAR(length=250), nullable=True),
    sa.Column('to_status', sa.VARCHAR(length=30), nullable=True),
    sa.Column('to_updated_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['conversion_id'], ['conversion.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction')
    op.drop_table('conversion')
    op.drop_table('wallet_payer')
    op.drop_table('token_pair')
    op.drop_table('conversion_fee')
    op.drop_table('token_detail')
    op.drop_table('blockchain_detail')
    # ### end Alembic commands ###
