# Code Integration Tool

## Overview

The Code Integration Tool is a simple yet powerful utility designed to streamline the process of sharing code with AI language models like ChatGPT. It addresses the common pain point of having to manually copy and paste multiple files or code snippets when discussing or reviewing code with AI assistants.

## Key Features

1. **Directory Integration**: Recursively scans a selected directory and its subdirectories for code files.
2. **Multiple File Types**: Supports various file types including .py, .js, .jsx, .ts, .tsx, .html, and .css.
3. **Prefix Path**: Option to add a custom prefix to file paths, useful for providing context to AI models.
4. **Code Statistics**: Provides total line count and non-empty line count for the integrated code.
5. **User-Friendly Interface**: Simple GUI for easy operation without needing command-line knowledge.

## How It Solves AI Interaction Pain Points

1. **Time-Saving**: Eliminates the need to manually copy and paste multiple files, saving significant time and effort.
2. **Context Preservation**: By including file paths and maintaining the directory structure, it helps AI models understand the context and relationships between different parts of your codebase.
3. **Comprehensive Code Sharing**: Allows sharing of entire project structures or specific directories with ease, ensuring no important code is missed.
4. **Formatting Consistency**: Maintains a consistent format for all integrated code, making it easier for AI models to parse and understand.
5. **Code Overview**: Provides instant statistics about the amount of code shared, helping users gauge the scope of their query to the AI.

## How to Use

1. Run the application.
2. Click "Browse" to select the directory containing your code.
3. (Optional) Enter a prefix path if you want to add context to your file structure.
4. Click "Integrate Code".
5. Choose where to save the integrated code file.
6. The tool will display statistics about the integrated code.
7. Copy the contents of the saved file and paste them into your conversation with the AI model.

## Usage Example

Let's say you have a React project with the following structure:

```
src/
  ├── app/
  │   ├── Flow.tsx
  │   └── common/
  │       └── alert-modal.tsx
```

After running the Code Integration Tool on the `src` directory with the prefix "app", you'll get an output file containing:

```typescript
// app/app/Flow.tsx
import { useCallback } from "react";
import {
  Background,
  Controls,
  MiniMap,
  ReactFlow,
  addEdge,
  useNodesState,
  useEdgesState,
  type OnConnect,
} from "@xyflow/react";
import "@xyflow/react/dist/style.css";
import { initialNodes, nodeTypes, type CustomNodeType } from "./nodes";
import { initialEdges, edgeTypes, type CustomEdgeType } from "./edges";

export default function App() {
  const [nodes, , onNodesChange] = useNodesState<CustomNodeType>(initialNodes);
  const [edges, setEdges, onEdgesChange] =
    useEdgesState<CustomEdgeType>(initialEdges);
  const onConnect: OnConnect = useCallback(
    (connection) => setEdges((edges) => addEdge(connection, edges)),
    [setEdges]
  );

  return (
    <ReactFlow<CustomNodeType, CustomEdgeType>
      nodes={nodes}
      nodeTypes={nodeTypes}
      onNodesChange={onNodesChange}
      edges={edges}
      edgeTypes={edgeTypes}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
      fitView
    >
      <Background />
      <MiniMap />
      <Controls />
    </ReactFlow>
  );
}

// app/app/common/alert-modal.tsx
("use client");

import { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogHeader,
  DialogContent,
  DialogTitle,
  DialogDescription,
} from "@/components/ui/dialog";

interface AlertModalProps {
  title: string;
  description: string;
  name?: string;
  loading: boolean;
  isOpen: boolean;
  onClose: () => void;
  onConfirm: () => void;
}

export const AlertModal = ({
  title,
  description,
  name,
  isOpen,
  onClose,
  onConfirm,
  loading,
}: AlertModalProps) => {
  console.log();
  const [isMounted, setIsMounted] = useState(false);

  useEffect(() => {
    setIsMounted(true);
  }, []);

  // ... rest of the component
};
```

The tool will also provide you with statistics:

```
Files integrated and saved to [your_output_file_path]

Total lines: 67
Non-empty lines: 61
```

You can then easily copy this entire output and paste it into your conversation with an AI model, providing a comprehensive view of your code structure and content.

## Benefits

- **Efficiency**: Drastically reduces the time needed to share large codebases or multiple files with AI.
- **Accuracy**: Ensures that all necessary code is included, reducing back-and-forth with AI for missing context.
- **Structure**: Maintains the project structure, helping AI understand the organization of your code.
- **Flexibility**: Works with various programming languages and file types commonly used in software development.

By using this tool, developers can have more productive and context-rich conversations with AI models, leading to better code reviews, more accurate problem-solving, and more efficient learning experiences.
