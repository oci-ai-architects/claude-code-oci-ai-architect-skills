#!/usr/bin/env python3
"""
OCI Diagram Generator - Wrapper Script
Uses Python diagrams library with official OCI icons

Usage:
    python generate_oci_diagram.py --type rag --output /path/to/output
    python generate_oci_diagram.py --type agent --output /path/to/output
    python generate_oci_diagram.py --type platform --output /path/to/output

Requirements:
    pip install diagrams
    # Graphviz must be installed (conda install graphviz or apt install graphviz)
"""

import argparse
from diagrams import Diagram, Cluster, Edge
from diagrams.oci.compute import VM, Container, OKE, Functions
from diagrams.oci.database import Autonomous, DatabaseService
from diagrams.oci.network import LoadBalancer, Vcn, InternetGateway, ServiceGateway
from diagrams.oci.storage import ObjectStorage, BlockStorage
from diagrams.oci.security import Vault, CloudGuard
from diagrams.oci.monitoring import Telemetry, Events
from diagrams.generic.compute import Rack
from diagrams.onprem.client import Users

# Oracle brand colors reference
ORACLE_COLORS = {
    "red": "#C74634",
    "red_dark": "#8B2500",
    "teal": "#2d5967",
    "black": "#312D2A",
    "gray": "#9e9892",
    "light_gray": "#f5f4f2",
    "white": "#FFFFFF"
}

# Standard graph attributes for Oracle branding
GRAPH_ATTR = {
    "fontsize": "18",
    "bgcolor": ORACLE_COLORS["white"],
    "fontcolor": ORACLE_COLORS["black"],
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.0",
    "fontname": "Helvetica Bold",
    "pad": "0.5",
    "dpi": "200"
}

NODE_ATTR = {
    "fontsize": "11",
    "fontname": "Helvetica",
    "fontcolor": ORACLE_COLORS["black"]
}

EDGE_ATTR = {
    "color": ORACLE_COLORS["black"],
    "penwidth": "1.5"
}


def create_rag_platform(output_path: str, title: str = "OCI Enterprise RAG Platform"):
    """Generate RAG architecture diagram."""
    with Diagram(
        title,
        show=False,
        filename=output_path,
        direction="TB",
        graph_attr=GRAPH_ATTR,
        node_attr=NODE_ATTR,
        edge_attr=EDGE_ATTR,
        outformat="png"
    ):
        users = Users("Enterprise Users")

        with Cluster("OCI Region", graph_attr={"bgcolor": ORACLE_COLORS["light_gray"]}):
            with Cluster("Public Subnet"):
                igw = InternetGateway("Internet Gateway")
                lb = LoadBalancer("Load Balancer")

            with Cluster("Private Subnet - Application"):
                with Cluster("OKE Cluster"):
                    chat_ui = Container("Chat UI")
                    rag_api = Container("RAG API")
                functions = Functions("Document Chunking")

            with Cluster("Private Subnet - AI Services"):
                genai_embed = Rack("OCI GenAI\nCohere Embed 4")
                genai_chat = Rack("OCI GenAI\nCohere Command A")

            with Cluster("Private Subnet - Data"):
                adb = Autonomous("Autonomous DB 23ai\nVector Search")
                storage = ObjectStorage("Documents")

            vault = Vault("OCI Vault")

        users >> igw >> lb >> chat_ui >> rag_api
        rag_api >> Edge(color=ORACLE_COLORS["red"]) >> genai_embed
        rag_api >> Edge(color=ORACLE_COLORS["red"]) >> genai_chat
        rag_api >> Edge(color=ORACLE_COLORS["red"]) >> adb
        storage >> functions >> genai_embed >> adb
        rag_api >> Edge(style="dashed") >> vault

    print(f"RAG diagram generated: {output_path}.png")


def create_agent_platform(output_path: str, title: str = "OCI Multi-Agent Orchestration"):
    """Generate multi-agent architecture diagram."""
    with Diagram(
        title,
        show=False,
        filename=output_path,
        direction="TB",
        graph_attr=GRAPH_ATTR,
        node_attr=NODE_ATTR,
        edge_attr=EDGE_ATTR,
        outformat="png"
    ):
        users = Users("Enterprise Users")

        with Cluster("OCI Region", graph_attr={"bgcolor": ORACLE_COLORS["light_gray"]}):
            lb = LoadBalancer("API Gateway")

            with Cluster("OCI GenAI Agent Hub", graph_attr={"bgcolor": "#fff5f3"}):
                supervisor = Rack("Supervisor Agent\nCohere Command A")

            with Cluster("Specialist Agents"):
                agents = [
                    Rack("Data Agent"),
                    Rack("SQL Agent"),
                    Rack("Code Agent"),
                    Rack("Report Agent")
                ]

            with Cluster("Tools"):
                select_ai = Functions("Select AI")
                rest_api = Functions("REST APIs")

            with Cluster("Data Layer"):
                adb = Autonomous("Autonomous DB 23ai")
                storage = ObjectStorage("Knowledge Base")

            vault = Vault("OCI Vault")

        users >> lb >> supervisor
        for agent in agents:
            supervisor >> Edge(color=ORACLE_COLORS["red"]) >> agent
        agents[0] >> Edge(style="dashed") >> select_ai
        agents[1] >> Edge(style="dashed") >> select_ai
        select_ai >> adb
        storage >> adb
        supervisor >> Edge(style="dotted") >> vault

    print(f"Agent diagram generated: {output_path}.png")


def create_ai_platform(output_path: str, title: str = "OCI Enterprise AI Platform"):
    """Generate general AI platform architecture diagram."""
    with Diagram(
        title,
        show=False,
        filename=output_path,
        direction="TB",
        graph_attr=GRAPH_ATTR,
        node_attr=NODE_ATTR,
        edge_attr=EDGE_ATTR,
        outformat="png"
    ):
        users = Users("Enterprise Users")

        with Cluster("OCI Region", graph_attr={"bgcolor": ORACLE_COLORS["light_gray"]}):
            with Cluster("Public Subnet"):
                igw = InternetGateway("Internet Gateway")
                lb = LoadBalancer("Load Balancer")

            with Cluster("Private Subnet - Compute"):
                with Cluster("OKE Cluster"):
                    apps = [Container("App-1"), Container("App-2"), Container("App-3")]

            with Cluster("Private Subnet - AI"):
                genai = Rack("OCI GenAI Service")
                ml = Rack("Data Science")

            with Cluster("Private Subnet - Data"):
                adb = Autonomous("Autonomous DB 23ai")
                storage = ObjectStorage("Object Storage")
                block = BlockStorage("Block Volume")

            with Cluster("Security"):
                vault = Vault("OCI Vault")
                guard = CloudGuard("Cloud Guard")

            telemetry = Telemetry("Observability")
            sgw = ServiceGateway("Service Gateway")

        users >> igw >> lb >> apps
        apps >> Edge(color=ORACLE_COLORS["red"]) >> genai
        apps >> Edge(color=ORACLE_COLORS["red"]) >> adb
        genai >> ml >> adb
        storage >> adb
        apps >> Edge(style="dashed") >> vault
        guard >> adb

    print(f"Platform diagram generated: {output_path}.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate OCI architecture diagrams")
    parser.add_argument("--type", choices=["rag", "agent", "platform"], required=True,
                        help="Diagram type: rag, agent, or platform")
    parser.add_argument("--output", required=True, help="Output file path (without extension)")
    parser.add_argument("--title", default=None, help="Custom diagram title")

    args = parser.parse_args()

    generators = {
        "rag": create_rag_platform,
        "agent": create_agent_platform,
        "platform": create_ai_platform
    }

    generator = generators[args.type]
    if args.title:
        generator(args.output, args.title)
    else:
        generator(args.output)
