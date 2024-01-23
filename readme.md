# FRC Robot Data WebSocket Server

This Python application is designed to receive information from FRC (FIRST Robotics Competition) robots using NTCore and WebSocket. It establishes a WebSocket server to make the received data accessible.

## Features

- Collect and transmit data from FRC robots using NTCore.
- Expose the data through a WebSocket server for real-time monitoring and analysis.

## Requirements

- Python 3.x
- NetworkTables (NTCore) library
- Websockets library

## Installation

1. Clone this repository to your local machine:

```bash
   git clone https://github.com/WoXy-Sensei/python-ntcore-websocket
```

## Usage

1. Start the FRC robot data server:

```bash
    py main.py
```

2. The WebSocket server will be accessible at `ws://127.0.0.1:8000`. You can connect to this WebSocket to receive real-time data from FRC robots.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Open an issue to discuss proposed changes or new features.
2. Fork the repository and create a new branch.
3. Make your changes and submit a pull request.

## License

This project is licensed under the MIT License.
