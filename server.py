import http.server
import socketserver
import csv

print("!!python server.py")
class MyHandler(http.server.SimpleHTTPRequestHandler):
    print("called")
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'

        if self.path.endswith('.html'):
            with open(self.path[1:], 'r') as f:
                html = f.read()
            with open('meta.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                table_data = ''
                for row in reader:
                    table_data += '<tr>'
                    for cell in row:
                        table_data += '<td>' + cell + '</td>'
                    table_data += '</tr>'
            html = html.replace('{{table_data}}', table_data)

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode())
        else:
            super().do_GET()

PORT = 8000
Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()