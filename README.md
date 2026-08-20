# MCP Deadbugz Simulator

A local simulation of the Deadbugz MCP supply-chain attack discovered by Pillar Security in August 2026.

## What this repo contains

Malicious MCP server with 3-call gate evasion technique
Python test harness to prove the attack works
Optional agent simulation with local LLM

## The attack pattern

1. Server shows benign tools for first 3 calls
2. 4th call triggers tools/listChanged notification
3. Tool descriptions mutate to credential-stealing instructions
4. AI agent follows malicious instructions

## Requirements

Python 3.10+
MCP SDK

## Usage

git clone https://github.com/anexbin/mcp-deadbugz-simulator.git
cd mcp-deadbugz-simulator
pip install -r requirements.txt
python server/malicious_server.py
python client/test_harness.py

## Files

server/malicious_server.py - The attack server
client/test_harness.py - Proof of concept
agent/local_agent.py - Optional LLM integration
configs/ - Example MCP configs

## Disclaimer

For educational and research purposes only.

## References

https://www.pillar.security/blog/deadbugz-currently-active-mcp-supply-chain-campaign
https://modelcontextprotocol.io

## License

MIT
