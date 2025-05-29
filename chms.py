import sqlite3
import argparse
from datetime import date

DB_NAME = 'chms.db'

# Database initialization

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS members (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT,
                    phone TEXT,
                    address TEXT,
                    birth_date TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS growth (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    member_id INTEGER NOT NULL,
                    status TEXT NOT NULL,
                    status_date TEXT NOT NULL,
                    FOREIGN KEY(member_id) REFERENCES members(id)
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS groups (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    zone TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS group_members (
                    group_id INTEGER NOT NULL,
                    member_id INTEGER NOT NULL,
                    PRIMARY KEY (group_id, member_id),
                    FOREIGN KEY(group_id) REFERENCES groups(id),
                    FOREIGN KEY(member_id) REFERENCES members(id)
                )''')
    c.execute('DROP TABLE IF EXISTS finances')
    c.execute('DROP TABLE IF EXISTS churches')

    c.execute('''CREATE TABLE IF NOT EXISTS churches (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS finances (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    church_id INTEGER NOT NULL,
                    type TEXT NOT NULL,  -- income or expense
                    amount REAL NOT NULL,
                    description TEXT,
                    entry_date TEXT NOT NULL,
                    FOREIGN KEY(church_id) REFERENCES churches(id)
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS certificates (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    member_id INTEGER NOT NULL,
                    certificate_type TEXT NOT NULL,
                    issue_date TEXT NOT NULL,
                    FOREIGN KEY(member_id) REFERENCES members(id)
                )''')
    conn.commit()
    conn.close()

# Member management

def add_member(args):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''INSERT INTO members (first_name, last_name, email, phone, address, birth_date)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (args.first_name, args.last_name, args.email, args.phone, args.address, args.birth_date))
    conn.commit()
    conn.close()
    print('Member added successfully.')


def list_members(args):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    for row in c.execute('SELECT id, first_name, last_name, email FROM members'):
        print(row)
    conn.close()

# Growth tracking

def add_growth(args):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''INSERT INTO growth (member_id, status, status_date)
                 VALUES (?, ?, ?)''',
              (args.member_id, args.status, args.status_date or date.today().isoformat()))
    conn.commit()
    conn.close()
    print('Growth status recorded.')

# Groups

def add_group(args):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''INSERT INTO groups (name, zone) VALUES (?, ?)''',
              (args.name, args.zone))
    conn.commit()
    conn.close()
    print('Group created.')


def assign_member(args):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''INSERT OR IGNORE INTO group_members (group_id, member_id) VALUES (?, ?)''',
              (args.group_id, args.member_id))
    conn.commit()
    conn.close()
    print('Member assigned to group.')

# Churches

def add_church(args):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO churches (name) VALUES (?)', (args.name,))
    conn.commit()
    conn.close()
    print('Church added.')


def list_churches(args):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    for row in c.execute('SELECT id, name FROM churches'):
        print(row)
    conn.close()

# Finances

def church_exists(conn, church_id):
    c = conn.cursor()
    c.execute('SELECT 1 FROM churches WHERE id=?', (church_id,))
    return c.fetchone() is not None


def add_finance(args):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    if not church_exists(conn, args.church_id):
        print('Church not found.')
        conn.close()
        return
    c.execute('''INSERT INTO finances (church_id, type, amount, description, entry_date)
                 VALUES (?, ?, ?, ?, ?)''',
              (args.church_id, args.type, args.amount, args.description,
               args.entry_date or date.today().isoformat()))
    conn.commit()
    conn.close()
    print('Financial entry recorded.')


def list_finances(args):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    if not church_exists(conn, args.church_id):
        print('Church not found.')
        conn.close()
        return
    for row in c.execute('''SELECT id, type, amount, description, entry_date
                            FROM finances WHERE church_id=?''',
                         (args.church_id,)):
        print(row)
    conn.close()


def update_finance(args):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    if not church_exists(conn, args.church_id):
        print('Church not found.')
        conn.close()
        return
    c.execute('SELECT id FROM finances WHERE id=? AND church_id=?',
              (args.id, args.church_id))
    if not c.fetchone():
        print('Finance entry not found for this church.')
        conn.close()
        return
    fields = []
    values = []
    if args.type:
        fields.append('type=?')
        values.append(args.type)
    if args.amount is not None:
        fields.append('amount=?')
        values.append(args.amount)
    if args.description is not None:
        fields.append('description=?')
        values.append(args.description)
    if args.entry_date:
        fields.append('entry_date=?')
        values.append(args.entry_date)
    if not fields:
        print('No fields to update.')
        conn.close()
        return
    values.append(args.id)
    c.execute(f'''UPDATE finances SET {", ".join(fields)} WHERE id=?''', values)
    conn.commit()
    conn.close()
    print('Finance entry updated.')


def delete_finance(args):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    if not church_exists(conn, args.church_id):
        print('Church not found.')
        conn.close()
        return
    c.execute('SELECT id FROM finances WHERE id=? AND church_id=?',
              (args.id, args.church_id))
    if not c.fetchone():
        print('Finance entry not found for this church.')
        conn.close()
        return
    c.execute('DELETE FROM finances WHERE id=?', (args.id,))
    conn.commit()
    conn.close()
    print('Finance entry deleted.')

# Certificates

def issue_certificate(args):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''INSERT INTO certificates (member_id, certificate_type, issue_date)
                 VALUES (?, ?, ?)''',
              (args.member_id, args.certificate_type, args.issue_date or date.today().isoformat()))
    conn.commit()
    conn.close()
    print('Certificate issued.')

# Argument parser setup

def main():
    parser = argparse.ArgumentParser(description='Simple Church Management System')
    subparsers = parser.add_subparsers(dest='command')

    parser_init = subparsers.add_parser('init', help='Initialize database')

    parser_add_member = subparsers.add_parser('add-member', help='Add a new member')
    parser_add_member.add_argument('first_name')
    parser_add_member.add_argument('last_name')
    parser_add_member.add_argument('--email', default='')
    parser_add_member.add_argument('--phone', default='')
    parser_add_member.add_argument('--address', default='')
    parser_add_member.add_argument('--birth-date', dest='birth_date', default='')
    parser_add_member.set_defaults(func=add_member)

    parser_list_members = subparsers.add_parser('list-members', help='List all members')
    parser_list_members.set_defaults(func=list_members)

    parser_growth = subparsers.add_parser('add-growth', help='Record growth status for a member')
    parser_growth.add_argument('member_id', type=int)
    parser_growth.add_argument('status')
    parser_growth.add_argument('--status-date', dest='status_date')
    parser_growth.set_defaults(func=add_growth)

    parser_group = subparsers.add_parser('add-group', help='Create a new group')
    parser_group.add_argument('name')
    parser_group.add_argument('--zone', default='')
    parser_group.set_defaults(func=add_group)

    parser_assign = subparsers.add_parser('assign-member', help='Assign member to a group')
    parser_assign.add_argument('group_id', type=int)
    parser_assign.add_argument('member_id', type=int)
    parser_assign.set_defaults(func=assign_member)

    parser_add_church = subparsers.add_parser('add-church', help='Add a new church')
    parser_add_church.add_argument('name')
    parser_add_church.set_defaults(func=add_church)

    parser_list_churches = subparsers.add_parser('list-churches', help='List churches')
    parser_list_churches.set_defaults(func=list_churches)

    parser_add_finance = subparsers.add_parser('add-finance', help='Record financial entry')
    parser_add_finance.add_argument('church_id', type=int)
    parser_add_finance.add_argument('type', choices=['income', 'expense'])
    parser_add_finance.add_argument('amount', type=float)
    parser_add_finance.add_argument('--description', default='')
    parser_add_finance.add_argument('--entry-date', dest='entry_date')
    parser_add_finance.set_defaults(func=add_finance)

    parser_list_fin = subparsers.add_parser('list-finances', help='List finances for a church')
    parser_list_fin.add_argument('church_id', type=int)
    parser_list_fin.set_defaults(func=list_finances)

    parser_update_fin = subparsers.add_parser('update-finance', help='Update a financial entry')
    parser_update_fin.add_argument('id', type=int)
    parser_update_fin.add_argument('church_id', type=int)
    parser_update_fin.add_argument('--type', choices=['income', 'expense'])
    parser_update_fin.add_argument('--amount', type=float)
    parser_update_fin.add_argument('--description')
    parser_update_fin.add_argument('--entry-date', dest='entry_date')
    parser_update_fin.set_defaults(func=update_finance)

    parser_delete_fin = subparsers.add_parser('delete-finance', help='Delete a financial entry')
    parser_delete_fin.add_argument('id', type=int)
    parser_delete_fin.add_argument('church_id', type=int)
    parser_delete_fin.set_defaults(func=delete_finance)

    parser_cert = subparsers.add_parser('certificate', help='Issue certificate for a member')
    parser_cert.add_argument('member_id', type=int)
    parser_cert.add_argument('certificate_type')
    parser_cert.add_argument('--issue-date', dest='issue_date')
    parser_cert.set_defaults(func=issue_certificate)

    args = parser.parse_args()

    if args.command == 'init':
        init_db()
        print('Database initialized.')
    elif hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
