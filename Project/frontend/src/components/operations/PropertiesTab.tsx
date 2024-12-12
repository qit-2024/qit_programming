import React, { useState } from 'react';
import { Card, Spin, Alert, Typography } from 'antd';
import { useDispatch, useSelector } from 'react-redux';
import { AppDispatch, RootState } from '../../store';
import { checkProperties } from '../../store/matrixSlice';
import { MatrixInput } from '../MatrixInput';
import { CheckCircleFilled, CloseCircleFilled } from '@ant-design/icons';
import { PropertiesResponse } from '../../types/matrix';

const { Text } = Typography;

export const PropertiesTab: React.FC = () => {
    const dispatch = useDispatch<AppDispatch>();
    const { loading, error } = useSelector((state: RootState) => state.matrix);
    const [properties, setProperties] = useState<PropertiesResponse | null>(null);

    const handleSubmit = async (matrix: number[][]) => {
        try {
            const result = await dispatch(checkProperties(matrix));
            if (checkProperties.fulfilled.match(result)) {
                setProperties(result.payload);
            }
        } catch (err) {
            console.error('Error checking properties:', err);
        }
    };

    return (
        <div className="space-y-4">
            <MatrixInput
                onSubmit={handleSubmit}
                title="Matrix for checking properties"
            />

            {loading && (
                <div className="flex justify-center mt-4">
                    <Spin size="large" />
                </div>
            )}

            {error && (
                <Alert
                    message="Error"
                    description={error}
                    type="error"
                    showIcon
                    className="mt-4"
                />
            )}

            {properties && (
                <Card title="Matrix properties" className="mt-4">
                    <div className="space-y-4">
                        <div className="flex items-center gap-2 my-2">
                            {properties.is_symmetric ? (
                                <CheckCircleFilled className="text-green-500 text-xl" />
                            ) : (
                                <CloseCircleFilled className="text-red-500 text-xl" />
                            )}
                            <Text>
                                Matrix {properties.is_symmetric ? 'is' : 'is not'} symmetrical
                            </Text>
                        </div>
                        <div className="flex items-center gap-2 my-2">
                            {properties.is_orthogonal ? (
                                <CheckCircleFilled className="text-green-500 text-xl" />
                            ) : (
                                <CloseCircleFilled className="text-red-500 text-xl" />
                            )}
                            <Text>
                                Matrix {properties.is_orthogonal ? 'is' : 'is not'} orthogonal
                            </Text>
                        </div>
                    </div>
                </Card>
            )}
        </div>
    );
};