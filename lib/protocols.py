

class Protocol():
    def __init__(self, name, ports, protos, nmap, only_ports, url, info):
        self.name = name
        self.defports = ports
        self.defproto = protos
        self.nmap = nmap
        self.only_ports = only_ports
        self.url = url
        self.info = info


general_protocol = Protocol("general", [""], [""], [""], False, "", "")

valid_protos = {
    "afp": Protocol("afp", ["548"], ["tcp"], ["afp"], False, "https://book.hacktricks.xyz/pentesting/584-pentesting-afp",
                  "The Apple Filing Protocol (AFP), formerly AppleTalk Filing Protocol, is a proprietary network protocol, and part of the Apple File Service (AFS), that offers file services for macOS and the classic Mac OS. In macOS, AFP is one of several file services supported. AFP currently supports Unicode file names, POSIX and access control listpermissions, resource forks, named extended attributes, and advanced file locking. In Mac OS 9 and earlier, AFP was the primary protocol for file services."),
    "ajp": Protocol("ajp", ["8009"], ["tcp"], ["ajp"], False, "https://book.hacktricks.xyz/pentesting/8009-pentesting-apache-jserv-protocol-ajp",
                  "AJP is a wire protocol. It an optimized version of the HTTP protocol to allow a standalone web server such as Apache to talk to Tomcat. Historically, Apache has been much faster than Tomcat at serving static content. The idea is to let Apache serve the static content when possible, but proxy the request to Tomcat for Tomcat related content."),
    "bacnet": Protocol("bacnet", ["47808"], ["udp"], ["BACNet"], False, "https://book.hacktricks.xyz/pentesting/47808-udp-bacnet",
                  "BACnet was designed to allow communication of building automation and control systems for applications such as heating, ventilating, and air-conditioning control (HVAC), lighting control, access control, and fire detection systems and their associated equipment. The BACnet protocol provides mechanisms for computerized building automation devices to exchange information, regardless of the particular building service they perform."),
    "cassandra": Protocol("cassandra", ["9160"], ["tcp"], ["cassandra"], False, "https://book.hacktricks.xyz/pentesting/cassandra",
                  "Apache Cassandra is a highly scalable, high-performance distributed database designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure. It is a type of NoSQL database. Let us first understand what a NoSQL database does."),
    "checkpoint": Protocol("checkpoint", ["264"], ["tcp"], [], False, "https://book.hacktricks.xyz/pentesting/pentesting-264-check-point-firewall-1",
                  "Check Point FireWall-1"),
    "couchdb": Protocol("couchdb", ["5984"], ["tcp"], [], False, "https://book.hacktricks.xyz/pentesting/5984-pentesting-couchdb",
                  "CouchDB is a document-oriented database and within each document fields are stored as key-value maps. Fields can be either a simple key/value pair, list, or map. Each document that is stored in the database is given a document-level unique identifier (_id) as well as a revision (_rev) number for each change that is made and saved to the database."),
    "dns": Protocol("dns", ["53"], ["udp"], ["domain"], True, "https://book.hacktricks.xyz/pentesting/pentesting-dns",
                  "The Domain Name Systems (DNS) is the phonebook of the Internet. Humans access information online through domain names, like nytimes.com or espn.com. Web browsers interact through Internet Protocol (IP) addresses. DN S translates domain names to IP addresses so browsers can load Internet resources."),
    "enip": Protocol("enip", ["44818"], ["tcp"], ["EtherNet/IP"], False, "https://book.hacktricks.xyz/pentesting/44818-ethernetip",
                  "EtherNet/IP is most commonly used in industrial automation control systems, such as for water processing plants, manufacturing facilities and utilities. Several control system vendors have developed programmable automation controllers and I/O capable of communicating via EtherNet/IP."),
    "finger": Protocol("finger", ["79"], ["tcp"], ["finger"], False, "https://book.hacktricks.xyz/pentesting/pentesting-finger",
                  "Finger is a program you can use to find information about computer users. It usually lists the login name, the full name, and possibly other details about the user you are fingering. These details may include the office location and phone number (if known), login time, idle time, time mail was last read, and the user's plan and project files."),
    "ftp": Protocol("ftp", ["21"], ["tcp"], ["ftp"], False, "https://book.hacktricks.xyz/pentesting/pentesting-ftp",
                  "The File Transfer Protocol (FTP) is a standard network protocol used for the transfer of computer files between a client and server on a computer network."),
    "https": Protocol("https", ["443", "10443", "1443", "80443"], ["tcp"], ["https", "ssl/http"], True, "https://book.hacktricks.xyz/pentesting/pentesting-web",
                  "HTTP means HyperText Transfer Protocol. HTTP is the underlying protocol used by the World Wide Web and this protocol defines how messages are formatted and transmitted, and what actions Web servers and browsers should take in response to various commands."),
    "http": Protocol("http", ["80", "1080", "8880", "8888", "9080", "9000", "10000", "10080"]+[str(i) for i in list(range(8000,8101))], ["tcp"], ["http"], True, "https://book.hacktricks.xyz/pentesting/pentesting-web",
                  "HTTP means HyperText Transfer Protocol. HTTP is the underlying protocol used by the World Wide Web and this protocol defines how messages are formatted and transmitted, and what actions Web servers and browsers should take in response to various commands."),
    "ike": Protocol("ike", ["500"], ["udp"], ["isakmp"], True, "https://book.hacktricks.xyz/pentesting/ipsec-ike-vpn-pentesting",
                  "IPsec is the most commonly used technology for both gateway-to-gateway (LAN-to-LAN) and host to gateway (remote access) enterprise VPN solutions. IKE is a type of ISAKMP (Internet Security Association Key Management Protocol) implementation, which is a framework for authentication and key exchange."),
    "imaps": Protocol("imaps", ["993"], ["tcp"], ["imaps"], False, "https://book.hacktricks.xyz/pentesting/pentesting-imap",
                  "As its name implies, IMAP allows you to access your email messages wherever you are; much of the time, it is accessed via the Internet. Basically, email messages are stored on servers. Whenever you check your inbox, your email client contacts the server to connect you with your messages. When you read an email message using IMAP, you aren't actually downloading or storing it on your computer; instead, you are reading it off of the server. As a result, it's possible to check your email from several different devices without missing a thing."),
    "imap": Protocol("imap", ["143"], ["tcp"], ["imap"], False, "https://book.hacktricks.xyz/pentesting/pentesting-imap",
                  "As its name implies, IMAP allows you to access your email messages wherever you are; much of the time, it is accessed via the Internet. Basically, email messages are stored on servers. Whenever you check your inbox, your email client contacts the server to connect you with your messages. When you read an email message using IMAP, you aren't actually downloading or storing it on your computer; instead, you are reading it off of the server. As a result, it's possible to check your email from several different devices without missing a thing."),
    "irc": Protocol("irc", ["6667", "6660–6669", "7000"], ["tcp"], ["irc"], False, "https://book.hacktricks.xyz/pentesting/pentesting-irc",
                  "IRC was originally a plain text protocol (although later extended), which on request was assigned port 194/TCP by IANA. However, the de facto standard has always been to run IRC on 6667/TCP and nearby port numbers (for example TCP ports 6660–6669, 7000) to avoid having to run the IRCd software with root privileges."),
    "iscsi": Protocol("iscsi", ["3260"], ["tcp"], ["iscsi"], False, "https://book.hacktricks.xyz/pentesting/3260-pentesting-iscsi",
                  "iSCSI is an acronym for Internet Small Computer Systems Interface, an Internet Protocol (IP)-based storage networking standard for linking data storage facilities. It provides block-level access to storage devices by carrying SCSI commands over a TCP/IP network. iSCSI is used to facilitate data transfers over intranets and to manage storage over long distances. It can be used to transmit data over local area networks (LANs), wide area networks (WANs), or the Internet and can enable location-independent data storage and retrieval."),
    "jrmi": Protocol("jrmi", ["1099"], ["tcp"], ["rmiregistry"], False, "https://book.hacktricks.xyz/pentesting/1099-pentesting-java-rmi",
                      "The Java Remote Method Invocation, or Java RMI, is a mechanism that allows an object that exists in one Java virtual machine to access and call methods that are contained in another Java virtual machine; This is basically the same thing as a remote procedure call, but in an object-oriented paradigm instead of a procedural one, which allows for communication between Java programs that are not in the same address space. One of the major advantages of RMI is the ability for remote objects to load new classes that aren't explicitly defined already, extending the behavior and functionality of an application."),
    "ldaps": Protocol("ldaps", ["636", "3269"], ["tcp"], [], False, "https://book.hacktricks.xyz/pentesting/pentesting-ldap",
                  "LDAP (Lightweight Directory Access Protocol) is a software protocol for enabling anyone to locate organizations, individuals, and other resources such as files and devices in a network, whether on the public Internet or on a corporate intranet. LDAP is a 'lightweight' (smaller amount of code) version of Directory Access Protocol (DAP). Typical LDAP ports are  389 and 636(ldaps) but Global Catalog is available by default on ports 3268, and 3269 for LDAPS."),
    "ldap": Protocol("ldap", ["389", "3268"], ["tcp"], ["ldap"], False, "https://book.hacktricks.xyz/pentesting/pentesting-ldap",
                  "LDAP (Lightweight Directory Access Protocol) is a software protocol for enabling anyone to locate organizations, individuals, and other resources such as files and devices in a network, whether on the public Internet or on a corporate intranet. LDAP is a 'lightweight' (smaller amount of code) version of Directory Access Protocol (DAP). Typical LDAP ports are  389 and 636(ldaps) but Global Catalog is available by default on ports 3268, and 3269 for LDAPS."),
    "memcache": Protocol("memcache", ["11211"], ["tcp"], [], False, "https://book.hacktricks.xyz/pentesting/11211-memcache",
                  "Memcache is a general-purpose distributed memory caching system. It is often used to speed up dynamic database-driven websites by caching data and objects in RAM to reduce the number of times an external data source (such as a database or API) must be read."),
    "modbus": Protocol("modbus", ["502"], ["tcp"], ["modbus"], False, "https://book.hacktricks.xyz/pentesting/pentesting-modbus",
                  "Modbus Protocol is a messaging structure developed by Modicon in 1979. It is used to establish master-slave/client-server communication between intelligent devices."),
    "mongodb": Protocol("mongodb", ["27017", "27018"], ["tcp"], ["mongodb "], False, "https://book.hacktricks.xyz/pentesting/27017-27018-mongodb",
                  "MongoDB is an open source database management system (DBMS) that uses a document-oriented database model which supports various forms of data."),
    "mssql": Protocol("mssql", ["1443"], ["tcp"], ["ms-sql"], False, "https://book.hacktricks.xyz/pentesting/pentesting-mssql-microsoft-sql-server",
                  "Microsoft SQL Server is a relational database management system developed by Microsoft. As a database server, it is a software product with the primary function of storing and retrieving data as requested by other software applications—which may run either on the same computer or on another computer across a network (including the Internet)."),
    "mysql": Protocol("mysql", ["3306"], ["tcp"], ["mysql"], False, "https://book.hacktricks.xyz/pentesting/pentesting-mysql",
                  "MySQL is a freely available open source Relational Database Management System (RDBMS) that uses Structured Query Language (SQL)."),
    "ndmp": Protocol("ndmp", ["10000"], ["tcp"], ["ndmp"], False, "https://book.hacktricks.xyz/pentesting/10000-network-data-management-protocol-ndmp",
                  "NDMP, or Network Data Management Protocol, is a protocol meant to transport data between network attached storage (NAS) devices and backup devices. This removes the need for transporting the data through the backup server itself, thus enhancing speed and removing load from the backup server."),
    "nfs": Protocol("nfs", ["2049"], ["tcp"], ["nfs"], False, "https://book.hacktricks.xyz/pentesting/nfs-service-pentesting",
                  "It is a client/server system that allows users to access files across a network and treat them as if they resided in a local file directory."),
    "ntp": Protocol("ntp", ["123"], ["udp"], ["ntp"], False, "https://book.hacktricks.xyz/pentesting/pentesting-ntp",
                  "The Network Time Protocol (NTP) is a networking protocol for clock synchronization between computer systems over packet-switched, variable-latency data networks."),
    "oracle": Protocol("oracle", ["1521","1522-1529"], ["tcp"], ["oracle-tns"], False, "https://book.hacktricks.xyz/pentesting/1521-1522-1529-pentesting-oracle-listener",
                  "Oracle database (Oracle DB) is a relational database management system (RDBMS) from the Oracle Corporation. You need to install some dependencied to pentest this service: https://book.hacktricks.xyz/pentesting/1521-1522-1529-pentesting-oracle-listener/oracle-pentesting-requirements-installation"),
    "pgsql": Protocol("pgsql", ["5432", "5433"], ["tcp"], ["pgsql"], False, "https://book.hacktricks.xyz/pentesting/pentesting-postgresql",
                  "PostgreQSL is an open source object-relational database system that uses and extends the SQL language."),
    "pjl": Protocol("pjl", ["9100"], ["tcp"], ["jetdirect"], False, "https://book.hacktricks.xyz/pentesting/9100-pjl",
                  "The Printer Job Language (PJL) was originally introduced by HP but soon became a de facto standard for print job control. ‘PJL resides above other printer languages’ and can be used to change settings like paper tray or size. It must however be pointed out that PJL is not limited to the current print job as some settings can be made permanent. PJL can also be used to change the printer's display or read/write files on the device. There are many dialects as vendors tend to support only a subset of the commands listed in the PJL reference and instead prefer to add proprietary ones."),
    "pops": Protocol("pops", ["995"], ["tcp"], ["pop3"], False, "https://book.hacktricks.xyz/pentesting/pentesting-pop",
                  "Post Office Protocol (POP) is a type of computer networking and Internet standard protocol that extracts and retrieves email from a remote mail server for access by the host machine. POP is an application layer protocol in the OSI model that provides end users the ability to fetch and receive email."),
    "pop": Protocol("pop", ["110"], ["tcp"], ["pop3"], False, "https://book.hacktricks.xyz/pentesting/pentesting-pop",
                  "Post Office Protocol (POP) is a type of computer networking and Internet standard protocol that extracts and retrieves email from a remote mail server for access by the host machine. POP is an application layer protocol in the OSI model that provides end users the ability to fetch and receive email."),
    "portmapper": Protocol("portmapper", ["111"], ["tcp"], ["rpcbind"], False, "https://book.hacktricks.xyz/pentesting/pentesting-rpcbind",
                  "Provides information between Unix based systems. Port is often probed, it can be used to fingerprint the Nix OS, and to obtain information about available services. Port used with NFS, NIS, or any rpc-based service."),
    "rdp": Protocol("rdp", ["3389"], ["tcp"], ["ms-wbt-server"], False, "https://book.hacktricks.xyz/pentesting/pentesting-rdp",
                  "Remote Desktop Protocol (RDP) is a proprietary protocol developed by Microsoft, which provides a user with a graphical interface to connect to another computer over a network connection. The user employs RDP client software for this purpose, while the other computer must run RDP server software"),
    "redis": Protocol("redis", ["6379"], ["tcp"], [], False, "https://book.hacktricks.xyz/pentesting/6379-pentesting-redis",
                  "Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broke."),
    "rexec": Protocol("rexec", ["512"], ["tcp"], ["exec"], False, "https://book.hacktricks.xyz/pentesting/512-pentesting-rexec",
                  "It is a service that allows you to execute a command inside a host if you know valid credentials (username and password)."),
    "rlogin": Protocol("rlogin", ["513"], ["tcp"], ["login"], False, "https://book.hacktricks.xyz/pentesting/pentesting-rlogin",
                  "This service was mostly used in the old days for remote administration but now because of security issues this service has been replaced by the slogin and the ssh."),
    "rsh": Protocol("rsh", ["514"], ["tcp"], [], False, "https://book.hacktricks.xyz/pentesting/pentesting-rsh",
                  "Rsh use .rhosts files and /etc/hosts.equiv for authentication. These methods relied on IP addresses and DNS (Domain Name System) for authentication."),
    "rsync": Protocol("rsync", ["873"], ["tcp"], ["rsync"], False, "https://book.hacktricks.xyz/pentesting/873-pentesting-rsync",
                  "rsync is a utility for efficiently transferring and synchronizing files between a computer and an external hard drive and across networked computers by comparing the modification timesand sizes of files.[3] It is commonly found on Unix-like operating systems. The rsync algorithm is a type of delta encoding, and is used for minimizing network usage. Zlib may be used for additional data compression,[3] and SSH or stunnel can be used for security."),
    "rtsp": Protocol("rtsp", ["554", "8554"], ["tcp"], ["rtsp"], False, "https://book.hacktricks.xyz/pentesting/554-8554-pentesting-rtsp",
                  "The Real Time Streaming Protocol (RTSP) is a network control protocol designed for use in entertainment and communications systems to control streaming media servers. The protocol is used for establishing and controlling media sessions between end points. Clients of media servers issue VHS-style commands, such as play, record and pause, to facilitate real-time control of the media streaming from the server to a client (Video On Demand) or from a client to the server (Voice Recording)."),
    "saprouter": Protocol("saprouter", ["3299"], ["tcp"], ["saprouter"], False, "https://book.hacktricks.xyz/pentesting/3299-pentesting-saprouter",
                  "Saprouter is basically a reverse proxy for SAP systems, typically sitting between the Internet and internal SAP systems. Its main purpose is to allow controlled access from hosts on the Internet to the internal SAP systems, since it allows for a finer grained control of SAP protocols than a typical firewall."),
    "scanner": Protocol("scanner", [""], ["tcp", "udp"], [], False, "",
                  "This module will scan the IP using nmap (one fast and on top ports, another fast in all the ports and another slower on all the ports) and udp-proto-scanner.pl"),
    "smb": Protocol("smb", ["445", "139"], ["tcp"], ["microsoft-ds", "netbios-ssn"], True, "https://book.hacktricks.xyz/pentesting/pentesting-smb",
                  "Server Message Block in modern language is also known as Common Internet File System. The system operates as an application-layer network protocol primarily used for offering shared access to files, printers, serial ports, and other sorts of communications between nodes on a network. For instance, on Windows, SMB can run directly over TCP/IP without the need for NetBIOS over TCP/IP. This will use, as you point out, port 445. On other systems, you’ll find services and applications using port 139. This means that SMB is running with NetBIOS over TCP/IP."),
    "smtps": Protocol("smtp", ["587", "465"], ["tcp"], [], False, "https://book.hacktricks.xyz/pentesting/pentesting-smtp",
                  "SMTP (Simple Mail Transfer Protocol) is a TCP/IP protocol used in sending and receiving e-mail. However, since it is limited in its ability to queue messages at the receiving end, it is usually used with one of two other protocols, POP3 or IMAP."),
    "smtp": Protocol("smtp", ["25"], ["tcp"], ["smtp"], False, "https://book.hacktricks.xyz/pentesting/pentesting-smtp",
                  "SMTP (Simple Mail Transfer Protocol) is a TCP/IP protocol used in sending and receiving e-mail. However, since it is limited in its ability to queue messages at the receiving end, it is usually used with one of two other protocols, POP3 or IMAP."),
    "snmp": Protocol("snmp", ["161", "162", "10161", "10162"], ["udp"], ["snmp"], False, "https://book.hacktricks.xyz/pentesting/pentesting-snmp",
                  "SNMP - Simple Network Management Protocol is a protocol used to monitor different devices in the network (like routers, switches, printers, IoTs...)."),
    "ssh": Protocol("ssh", ["22"], ["tcp"], ["ssh"], False, "https://book.hacktricks.xyz/pentesting/pentesting-ssh",
                  "SSH or Secure Shell or Secure Socket Shell, is a network protocol that gives users a secure way to access a computer over an unsecured network."),
    "telnet": Protocol("telnet", ["23"], ["tcp"], ["telnet"], False, "https://book.hacktricks.xyz/pentesting/pentesting-telnet",
                  "Telnet is a network protocol that gives users a UNsecure way to access a computer over a network."),
    "vnc": Protocol("vnc", ["5900", "5901", "5800", "5801"], ["tcp"], ["vnc"], False, "https://book.hacktricks.xyz/pentesting/pentesting-vnc",
                  "In computing, Virtual Network Computing (VNC) is a graphical desktop-sharing system that uses the Remote Frame Buffer protocol (RFB) to remotely control another computer. It transmits the keyboard and mouse events from one computer to another, relaying the graphical-screen updates back in the other direction, over a network. "),
    "wrpc": Protocol("wrpc", ["135"], ["tcp"], ["msrpc"], True, "https://book.hacktricks.xyz/pentesting/135-penstesting-wrpc",
                  "Microsoft Remote Procedure Call, also known as a function call or a subroutine call, is a protocol that uses the client-server model in order to allow one program to request service from a program on another computer without having to understand the details of that computer's network. MSRPC was originally derived from open source software but has been developed further and copyrighted by Microsoft."),
    "x11": Protocol("x11", ["6000"], ["tcp"], ["X11"], False, "https://book.hacktricks.xyz/pentesting/6000-pentesting-x11",
                  "The X Window System (aka X) is a windowing system for bitmap displays, which is common on UNIX-based operating systems. X provides the basic framework for a GUI based environment. X also does not mandate the user interface – individual programs handle this."),
}
