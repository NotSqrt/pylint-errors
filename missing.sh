#!/usr/bin/env bash

FOUND=/tmp/found.txt
EXPECTED=/tmp/expected.txt
FULL_LIST=/tmp/fill_list.txt

LETTER=$1
LOWER_LETTER=${LETTER,,}
FILE=errors_$LOWER_LETTER.py

python /usr/local/bin/pylint --msg-template='{msg_id}' --module-rgx=.* --reports=n --persistent=n $FILE | egrep -o "$LETTER[0-9]{4}" | sort | uniq > $FOUND
egrep -o "$LETTER[0-9]{4}" $FILE | sort | uniq > $EXPECTED
python get_message_list.py | egrep -o "$LETTER[0-9]{4}" | sort | uniq > $FULL_LIST

echo $LETTER
colordiff $EXPECTED $FOUND

echo missing
colordiff $FULL_LIST $EXPECTED

echo