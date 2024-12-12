import React, { useState } from 'react';
import { Input, Button, Space, Card, InputNumber } from 'antd';
import { PlusOutlined, MinusOutlined } from '@ant-design/icons';

interface MatrixInputProps {
  onSubmit: (matrix: number[][]) => void;
  initialSize?: number;
  title?: string;
}

export const MatrixInput: React.FC<MatrixInputProps> = ({ 
  onSubmit, 
  initialSize = 3,
  title = 'Matrix input' 
}) => {
  const [size, setSize] = useState(initialSize);
  const [matrix, setMatrix] = useState<number[][]>(
    Array(size).fill(null).map(() => Array(size).fill(0))
  );

  const handleChange = (row: number, col: number, value: number | null) => {
    const newMatrix = matrix.map((r, i) =>
      r.map((c, j) => (i === row && j === col ? (value || 0) : c))
    );
    setMatrix(newMatrix);
  };

  const handleSizeChange = (newSize: number) => {
    const newMatrix = Array(newSize).fill(null)
      .map((_, i) => Array(newSize).fill(null)
        .map((_, j) => i < matrix.length && j < matrix[0].length ? matrix[i][j] : 0)
      );
    setSize(newSize);
    setMatrix(newMatrix);
  };

  return (
    <Card title={title} className="matrix-input-card">
      <Space direction="vertical" size="large">
        <Space>
          <Button 
            icon={<MinusOutlined />} 
            onClick={() => handleSizeChange(Math.max(2, size - 1))}
          />
          <span>Size: {size}x{size}</span>
          <Button 
            icon={<PlusOutlined />} 
            onClick={() => handleSizeChange(size + 1)}
          />
        </Space>

        <div className="matrix-grid">
          {matrix.map((row, i) => (
            <div key={i} className="matrix-row">
              {row.map((value, j) => (
                <InputNumber
                  key={`${i}-${j}`}
                  size="small"
                  value={value}
                  onChange={(val) => handleChange(i, j, val)}
                  className="matrix-cell"
                />
              ))}
            </div>
          ))}
        </div>

        <Button type="primary" onClick={() => onSubmit(matrix)}>
          Calculate
        </Button>
      </Space>
    </Card>
  );
};