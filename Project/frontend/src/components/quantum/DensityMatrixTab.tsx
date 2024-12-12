import React, { useState } from 'react';
import { Card, Input, Button, Switch, Space, Spin, Alert, Typography, Table } from 'antd';
import { PlusOutlined, MinusOutlined } from '@ant-design/icons';
import { ComplexNumber, DensityMatrixResult } from '../../types/quantum';
import { quantumService } from '../../services/quantumService';

const { Title, Text } = Typography;

interface ComplexInputProps {
  value: ComplexNumber;
  onChange: (value: ComplexNumber) => void;
}

const ComplexInput: React.FC<ComplexInputProps> = ({ value, onChange }) => (
  <Space>
    <Input
      type="number"
      value={value.real}
      onChange={e => onChange({ ...value, real: parseFloat(e.target.value) || 0 })}
      placeholder="Re"
      style={{ width: 80 }}
    />
    <span>+</span>
    <Input
      type="number"
      value={value.imag}
      onChange={e => onChange({ ...value, imag: parseFloat(e.target.value) || 0 })}
      placeholder="Im"
      style={{ width: 80 }}
    />
    <span>i</span>
  </Space>
);

export const DensityMatrixTab: React.FC = () => {
  const [isComplex, setIsComplex] = useState(false);
  const [stateVector, setStateVector] = useState<(number | ComplexNumber)[]>([
    isComplex ? { real: 1, imag: 0 } : 1,
    isComplex ? { real: 0, imag: 0 } : 0
  ]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<DensityMatrixResult | null>(null);

  const handleAddComponent = () => {
    setStateVector([
      ...stateVector,
      isComplex ? { real: 0, imag: 0 } : 0
    ]);
  };

  const handleRemoveComponent = (index: number) => {
    if (stateVector.length > 2) {
      setStateVector(stateVector.filter((_, i) => i !== index));
    }
  };

  const handleComponentChange = (index: number, value: number | ComplexNumber) => {
    const newVector = [...stateVector];
    newVector[index] = value;
    setStateVector(newVector);
  };

  const handleCalculate = async () => {
    try {
      setLoading(true);
      setError(null);
      const result = await quantumService.calculateDensityMatrix(stateVector, isComplex);
      setResult(result);
    } catch (err: any) {
      const errorMessage = err.response?.data?.error ||
        err.message ||
        'An unknown error occurred';
      setError(errorMessage);
      setResult(null);
    } finally {
      setLoading(false);
    }
  };

  const formatComplex = (num: ComplexNumber): string => {
    const real = parseFloat(num.real.toFixed(4));
    const imag = parseFloat(num.imag.toFixed(4));
    if (Math.abs(imag) < 1e-10) return real.toString();
    const sign = imag >= 0 ? '+' : '';
    return `${real}${sign}${imag}i`;
  };

  return (
    <div className="space-y-4">
      <Card title="Quantum state vector">
        <Space direction="vertical" className="w-full">
          <Space>
            <Text>Complex numbers:</Text>
            <Switch
              checked={isComplex}
              onChange={(checked) => {
                setIsComplex(checked);
                setStateVector(
                  stateVector.map(v =>
                    checked
                      ? (typeof v === 'number' ? { real: v, imag: 0 } : v)
                      : (typeof v === 'number' ? v : v.real)
                  )
                );
              }}
            />
          </Space>

          {stateVector.map((component, index) => (
            <Space key={index} align="center">
              <Text>|{index}⟩:</Text>
              {isComplex ? (
                <ComplexInput
                  value={component as ComplexNumber}
                  onChange={(value) => handleComponentChange(index, value)}
                />
              ) : (
                <Input
                  type="number"
                  value={component as number}
                  onChange={e => handleComponentChange(index, parseFloat(e.target.value) || 0)}
                  style={{ width: 120 }}
                />
              )}
              {stateVector.length > 2 && (
                <Button
                  type="text"
                  icon={<MinusOutlined />}
                  onClick={() => handleRemoveComponent(index)}
                  danger
                />
              )}
            </Space>
          ))}

          <Space className="mt-4">
            <Button
              type="dashed"
              icon={<PlusOutlined />}
              onClick={handleAddComponent}
            >
              Add component
            </Button>
            <Button
              type="primary"
              onClick={handleCalculate}
              loading={loading}
            >
              Calculate the density matrix
            </Button>
          </Space>
        </Space>
      </Card>

      {error && (
        <Alert
          message="Error of calculation"
          description={error}
          type="error"
          showIcon
          closable
          onClose={() => setError(null)}
          className="mb-4"
        />
      )}

      {loading && (
        <div className="flex justify-center py-8">
          <Spin size="large"/>
        </div>
      )}

      {result && !loading && (
        <Card title="Результаты">
          <Space direction="vertical" className="w-full">
            <Title level={4}>Density Matrix</Title>
            <Table
              dataSource={result.densityMatrix.map((row, i) => ({
                key: i,
                ...row.reduce((acc, cell, j) => ({
                  ...acc,
                  [`col${j}`]: formatComplex(cell)
                }), {})
              }))}
              columns={result.densityMatrix[0].map((_, index) => ({
                title: `|${index}⟩`,
                dataIndex: `col${index}`,
                key: `col${index}`,
                align: 'center' as const
              }))}
              pagination={false}
              bordered
              className="mb-4"
            />

            <Title level={4}>Properties:</Title>
            <ul className="list-none space-y-2">
              <li>
                <Text strong>Trace: </Text>
                <Text>{result.properties.trace.toFixed(4)}</Text>
              </li>
              <li>
                <Text strong>Hermitian: </Text>
                <Text>{result.properties.isHermitian ? 'Yes' : 'No'}</Text>
              </li>
              <li>
                <Text strong>Positive definite: </Text>
                <Text>{result.properties.isPositive ? 'Yes' : 'No'}</Text>
              </li>
              <li>
                <Text strong>Purity: </Text>
                <Text>{result.properties.purity.toFixed(4)}</Text>
              </li>
            </ul>
          </Space>
        </Card>
      )}
    </div>
  );
};  