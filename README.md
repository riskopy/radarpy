# radarpy
Radarpy helps system admins and researchers map our an infrastructure's install base. It's a cross-platform program that runs in the background, and checks for installed applications, services and commands (Windows, OS X and Linux). This helps in aggregating installations of various programs and their versions for detecting vulnerable installations, policy compliance or software research. The application list can then be exported to JSON, XML, CSV or transfered to service accepting requests. 

## Requirements
Packages required:
- Python 2.7+
- lxml

Most of the program calls on the Python standard library.

## Immediate To Do 
- Build Windows application detection
- Build Linux application detection
- Export application list to JSON
- Export application list to CSV
- Export application list to XML
- Transfer application list to another service through POST / GET requests

## Contributing
Always looking for contributions. So please refer to the To Do above, or please feel free to suggest.

How to contribute:
1. Fork radarpy
2. Create a branch (git checkout -b my_radarpy)
3. Commit your changes (git commit -am "Added lasers. Pew pew pew!")
4. Push to the branch (git push origin my_radarpy)
5. Open a Pull Request
6. Enjoy the liberating sensation of open source and wait

## License 
MIT License. Riskopy has the right to modify the radarpy's license at any point in time. 