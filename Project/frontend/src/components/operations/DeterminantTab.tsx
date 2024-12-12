import React, { useState } from 'react';  
import { Card, Button, Spin, Alert, Typography } from 'antd';
import { MatrixInput } from '../MatrixInput'; 
import {calculateDeterminant} from '../../store/matrixSlice';
import type { Matrix } from '../../types/matrix';  
import { useDispatch } from 'react-redux';
import { AppDispatch } from '../../store';

const { Title } = Typography;  

export const DeterminantTab: React.FC = () => {
  const dispatch = useDispatch<AppDispatch>();

  const [loading, setLoading] = useState(false);  
  const [error, setError] = useState<string | null>(null);  
  const [result, setResult] = useState<number | null>(null);  

  const handleCalculate = async (matrix: Matrix) => {  
    try {  
      setLoading(true);  
      setError(null);  

      const response = await dispatch(calculateDeterminant(matrix));  

      setResult(response.payload.determinant);
    } catch (err) {  
      setError(err instanceof Error ? err.message : 'An unknown error occurred');  
    } finally {  
      setLoading(false);  
    }  
  };  

  return (  
    <div className="space-y-4">  
      <MatrixInput  
        onSubmit={handleCalculate}  
        title="Matrix for calculating determinant"  
      />  
      
      {error && (  
        <Alert  
          message="Error"  
          description={error}  
          type="error"  
          showIcon  
          className="mt-4"  
        />  
      )}  
      
      {loading ? (  
        <div className="flex justify-center mt-4">  
          <Spin size="large" />  
        </div>  
      ) : result !== null && (  
        <Card title="Result" className="mt-4">  
          <Title level={4}>  
            Determinant: {result.toFixed(4)}  
          </Title>  
        </Card>  
      )}  
    </div>  
  );  
};  
