As part of this assignment for the course Computer Networks, we wrote client and server programs that implement the following functionalities (Taken from the assignment question given by Prof. Mahavir Jhawar).

1. Overall Goal

• Server side program will be running simultaneously at three different PCs.
• Let L = (x1, x2, . . . , x10) be a list of 10 integers.
• Each server will be holding a copy of this list, say Li = (x1, x2, . . . , x10), where i = 1, 2, 3.
• Each server will be listening, and accepting requests from different clients, who want to shuffle any two entries in the L that is presented to them by the accepting server.
• The task at hand is that eventually, each server should hold the same copy of L even after executing the requests that they have received from different clients.
• In principle, this is possible if the servers are able to order these requests using the time stamp that they are carrying.


2. Request-admission Phase: Client to Server Communication

• In this phase, any client can connect to any server.
• After successful connection to the server, the client is presented with a list L = (x1, x2, . . . , x10) that the server is currently holding.
• The client make a request by providing a tuple (i, j) as input - meaning "shuffle ith and jth entry of L".
• Server accepts the request and close the connection


3. Time-stamp Based Consensus Phase: Server to Server Communication

• In this phase, the servers connect to each other to order the requests.
• Each server connects to the other two servers to exchange the requests that it has received.
• Each server will eventually collect all requests and order them as per the time
stamp.
• Each server will apply shuffle updates to its own copy of the list - against the
ordered requests in sequence

4. Conditional Time-stamp Based Consensus Phase: Server to Server Communication. 
The Extra-Credit directory in this repository contains the working model with this additional functionality.

• Each server connects to the other two servers to exchange the requests that it has received.
• Each server also exchange the ip addresses of the requester.
• Each server will eventually collect all requests and order them as per the time stamp, except that it is now configured to give priority to a specific sender ip address (and all three servers have agreed on this specific ip offline).
• Each server will apply shuffle updates to its own copy of the list - against the
ordered requests.
