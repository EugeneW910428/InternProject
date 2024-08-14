import socket
import dxfgrabber

def send_data_to_csharp(data):
    host = 'localhost' 
    port = 12345  

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the C# application
        client_socket.connect((host, port))

        # Send data
        client_socket.sendall(data.encode('utf-8'))
        print("Data sent to C# application.")
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        # Close the socket
        client_socket.close()

def read_dxf_and_collect_output(file_path):
    dxf = dxfgrabber.readfile(file_path)
    text_data = ""

    #text_data += "Layers:\n"
    #for layer in dxf.layers:
        #text_data += f"{layer.name}  Color: {layer.color}  Linetype: {layer.linetype}\n"

    #text_data += "\nEntities:\n"
    for e in dxf.entities:
        #text_data += f"DXF Type: {e.dxftype}, Layer: {e.layer}\n"
        if e.dxftype == 'LINE':
            text_data += f"  Start: {e.start}, End: {e.end}\n"
        elif e.dxftype == 'CIRCLE':
            text_data += f"  Center: {e.center}, Radius: {e.radius}\n"
        elif e.dxftype == 'ARC':
            text_data += f"  Center: {e.center}, Radius: {e.radius}, Start Angle: {e.start_angle}, End Angle: {e.end_angle}\n"
        elif e.dxftype == 'POINT':
            text_data += f"  Point: {e.point}\n"
        text_data += "@\r\n"

    return text_data


if __name__ == "__main__":
    dxf_file_path = "POINT_O.dxf"
    dxf_output = read_dxf_and_collect_output(dxf_file_path)
    send_data_to_csharp(dxf_output)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Note that C# application need to run first, then run the python code via terminal. 

