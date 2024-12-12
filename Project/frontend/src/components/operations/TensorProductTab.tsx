import React, { useState } from 'react';
import { Card, Button, Spin, Alert, Typography, Space, Table } from 'antd';
import { useDispatch, useSelector } from 'react-redux';
import { AppDispatch, RootState } from '../../store';
import { calculateTensorProduct } from '../../store/matrixSlice';
import { MatrixInput } from '../MatrixInput';
import './TensorProductTab.scss';

const { Text } = Typography;

export const TensorProductTab: React.FC = () => {
    const dispatch = useDispatch<AppDispatch>();
    const { loading, error } = useSelector((state: RootState) => state.matrix);

    const [matrixA, setMatrixA] = useState<number[][]>([]);
    const [matrixB, setMatrixB] = useState<number[][]>([]);
    const [isMatrixASet, setIsMatrixASet] = useState(false);
    const [isMatrixBSet, setIsMatrixBSet] = useState(false);
    const [tensorResult, setTensorResult] = useState<number[][] | null>(null);

    const handleCalculate = async () => {
        if (matrixA.length > 0 && matrixB.length > 0) {
            try {
                const result = await dispatch(calculateTensorProduct({
                    matrix_a: matrixA,
                    matrix_b: matrixB
                })).unwrap();

                if (result && result.result) {
                    setTensorResult(result.result);
                }
            } catch (err) {
                console.error('Error calculating tensor product:', err);
            }
        }
    };

    const renderResultTable = (matrix: number[][]) => {
        const columns = matrix[0].map((_, index) => ({
            title: `${index + 1}`,
            dataIndex: `col${index}`,
            key: `col${index}`,
            align: 'center' as const,
            width: 80,
        }));

        const dataSource = matrix.map((row, rowIndex) => ({
            key: rowIndex,
            ...row.reduce((acc, cell, colIndex) => ({
                ...acc,
                [`col${colIndex}`]: cell.toFixed(2)
            }), {})
        }));

        return (
            <Table
                dataSource={dataSource}
                columns={columns}
                pagination={false}
                bordered
                size="middle"
                className="w-full"
                scroll={{ x: 'max-content' }}
            />
        );
    };

    return (
        <div className="space-y-6 matrix-container">
            <Space direction="vertical" size="large" className="w-full">
                <Space direction='horizontal'>
                <Card title="Matrix A">
                        <MatrixInput
                            onSubmit={(matrix) => {
                                setMatrixA(matrix);
                                setIsMatrixASet(true);
                            }}
                            initialSize={2}
                        />
                    </Card>

                    <Card title="Matrix B">
                        <MatrixInput
                            onSubmit={(matrix) => {
                                setMatrixB(matrix);
                                setIsMatrixBSet(true);
                            }}
                            initialSize={2}
                        />
                    </Card>
                </Space>
            

                <Button
                    type="primary"
                    onClick={handleCalculate}
                    disabled={!isMatrixASet || !isMatrixBSet}
                    loading={loading}
                    className="w-full"
                >
                    Calculate tensor product
                </Button>
            </Space>
            <Space className='result-container'>
                {error && (
                    <Alert
                        message="Error"
                        description={error}
                        type="error"
                        showIcon
                    />
                )}

                {loading && (
                    <div className="flex justify-center">
                        <Spin size="large" />
                    </div>
                )}

                {tensorResult && (
                    <Card
                        title={
                            <div className="flex items-center justify-between">
                                <span>Result of the tensor product</span>
                                <Text type="secondary">
                                    Size: {tensorResult.length} × {tensorResult[0]?.length}
                                </Text>
                            </div>
                        }
                    >
                        <div className="overflow-x-auto">
                            {renderResultTable(tensorResult)}
                        </div>
                    </Card>
                )}
            </Space>
        </div>
    );
};