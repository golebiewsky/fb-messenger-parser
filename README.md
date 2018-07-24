# fb-messenger-parser
Parse and search through Facebook messenger messages.

## Description

This is a simple script for parsing and searching through Facebook messenger messages, exported directly from Facebook as json files. Instructions on how to export messages in the [link](https://www.facebook.com/help/1701730696756992?helpref=hc_global_nav).

Script at the moment has the basic ability to parse message files in directories (as downloaded from Facebook and uncompressed) and provides basic case-sensitive search.

Work in progress.

## Usage

Execute the script and follow on screen instructions
    
    $ python fb-messenger-parser.py
    Set the base directory for facebook messenger messages (exported as json): example
    Search text: How
    ---------------------------
    Message content: "How are you doing?"
    Sender name: James Smith
    Timestamp: 2015-04-18 12:07:01
    Conversation title: John Doe
    ---------------------------
    Message content: "I am fine! How are you?"
    Sender name: John Doe
    Timestamp: 2015-04-18 12:06:40
    Conversation title: John Doe
