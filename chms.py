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
    c.execute('''CREATE TABLE IF NOT EXISTS finances (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT NOT NULL,  -- income or expense
                    amount REAL NOT NULL,
                    description TEXT,
                    entry_date TEXT NOT NULL
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

# Finances

def record_finance(args):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''INSERT INTO finances (type, amount, description, entry_date)
                 VALUES (?, ?, ?, ?)''',
              (args.type, args.amount, args.description, args.entry_date or date.today().isoformat()))
    conn.commit()
    conn.close()
    print('Financial entry recorded.')

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

    parser_finance = subparsers.add_parser('finance', help='Record financial entry')
    parser_finance.add_argument('type', choices=['income', 'expense'])
    parser_finance.add_argument('amount', type=float)
    parser_finance.add_argument('--description', default='')
    parser_finance.add_argument('--entry-date', dest='entry_date')
    parser_finance.set_defaults(func=record_finance)

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
