"""init

Revision ID: 6d8086b2ca11
Revises: 
Create Date: 2022-05-20 09:11:42.412343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d8086b2ca11'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('competitionsDB',
    sa.Column('competition_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('competition_id', name=op.f('pk_competitionsDB'))
    )
    op.create_table('participantsDB',
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('participant_first_name', sa.String(), nullable=True),
    sa.Column('participant_last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('participant_id', name=op.f('pk_participantsDB'))
    )
    op.create_table('backlogDB',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fighter_id', sa.Integer(), nullable=True),
    sa.Column('competition_id', sa.Integer(), nullable=True),
    sa.Column('round_number', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['competition_id'], ['competitionsDB.competition_id'], name=op.f('fk_backlogDB_competition_id_competitionsDB')),
    sa.ForeignKeyConstraint(['fighter_id'], ['participantsDB.participant_id'], name=op.f('fk_backlogDB_fighter_id_participantsDB')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_backlogDB'))
    )
    op.create_table('registrationsDB',
    sa.Column('reg_id', sa.Integer(), nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=True),
    sa.Column('competition_id', sa.Integer(), nullable=True),
    sa.Column('activity_status', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['competition_id'], ['competitionsDB.competition_id'], name=op.f('fk_registrationsDB_competition_id_competitionsDB')),
    sa.ForeignKeyConstraint(['participant_id'], ['participantsDB.participant_id'], name=op.f('fk_registrationsDB_participant_id_participantsDB')),
    sa.PrimaryKeyConstraint('reg_id', name=op.f('pk_registrationsDB'))
    )
    op.create_table('fightsDB',
    sa.Column('fight_id', sa.Integer(), nullable=False),
    sa.Column('competition_id', sa.Integer(), nullable=True),
    sa.Column('round_number', sa.Integer(), nullable=True),
    sa.Column('red_fighter_id', sa.Integer(), nullable=True),
    sa.Column('blue_fighter_id', sa.Integer(), nullable=True),
    sa.Column('fight_winner_id', sa.Integer(), nullable=True),
    sa.Column('final_status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['blue_fighter_id'], ['registrationsDB.reg_id'], name=op.f('fk_fightsDB_blue_fighter_id_registrationsDB')),
    sa.ForeignKeyConstraint(['competition_id'], ['competitionsDB.competition_id'], name=op.f('fk_fightsDB_competition_id_competitionsDB')),
    sa.ForeignKeyConstraint(['red_fighter_id'], ['registrationsDB.reg_id'], name=op.f('fk_fightsDB_red_fighter_id_registrationsDB')),
    sa.PrimaryKeyConstraint('fight_id', name=op.f('pk_fightsDB'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fightsDB')
    op.drop_table('registrationsDB')
    op.drop_table('backlogDB')
    op.drop_table('participantsDB')
    op.drop_table('competitionsDB')
    # ### end Alembic commands ###
