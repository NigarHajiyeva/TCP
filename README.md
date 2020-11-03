# TCP Text Service

## Scenario
You as a software developer must create the client-server-based console app **“text_service”**.
With the next abilities:

**Change text**: The sender sends the text file to the server and the json file, in respond the server
must read the json file and swap the words from the text according the json file.

**Encode/Decode text**: The sender sends the text file and the key (another text) on the respond
the server must XOR the text message with the key (One Time Pad cipher) and return it to the
client. The decoding process happens in the same way where instead of the text message the
client sends 
## Installation 
Clone repository into your directory:

    git clone https://github.com/NigarHajiyeva/TCP.git

Install requirements for this application:

    pip install -r requirements.txt

## Usage

To use this application, open 2 terminal tabs for **Server** and **Client**. For **Server**, run following command:

    python3 text_service.py server ""

"" -> interface for server.

To specify port use -p *port_number* (-p 1234). But, by default, port number is given (5432)

For *Client*, use the following commands:

*Change Text*:

    python3 text_service.py hostname --mode change_text text_file.txt json_file.json

*Encode_Decode*:

    python3 text_service.py hostname --mode encode_decode text_file.txt key.txt
    
To stop server, head to **Server** terminal and press `Ctrl+C` in terminal.
