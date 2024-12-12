import React from 'react';
import { Card, Spin, Table, Typography } from 'antd';
import { useDispatch, useSelector } from 'react-redux';
import { AppDispatch, RootState } from '../../../store';
import { calculateEigenvalues } from '../../../store/matrixSlice';
import { MatrixInput } from '../../MatrixInput';
import { eigenvalueColumns } from './EigenvaluesTab.const';
import { getEigenvaluesData, getEigenvectorColumns, getEigenvectorsData } from './EigenValuesTab.utils';

const { Title } = Typography;


export const EigenvaluesTab: React.FC = () => {
  const dispatch = useDispatch<AppDispatch>();
  const { results, loading } = useSelector((state: RootState) => state.matrix);


  const eigenvaluesData = getEigenvaluesData(results.eigenvalues);

  const eigenvectorsData = getEigenvectorsData(results.eigenvalues);


  const eigenvectorColumns = getEigenvectorColumns(results.eigenvalues);

  return (
    <div className="space-y-4">
      <MatrixInput
        onSubmit={(matrix) => dispatch(calculateEigenvalues(matrix))}
        title="Matrix for calculating eigenvalues and eigenvectors"
      />

      {loading ? (
        <div className="flex justify-center py-8">
          <Spin size="large" />
        </div>
      ) : results.eigenvalues && (
        <Card title="Results" className="mt-4">
          <div className="space-y-6">
            <div>
              <Title level={5}>Eigenvalues:</Title>
              <Table
                dataSource={eigenvaluesData}
                columns={eigenvalueColumns}
                pagination={false}
                bordered
                size="middle"
                className="mb-4"
              />
            </div>

            <div>
              <Title level={5}>Eigenvectors:</Title>
              <Table
                dataSource={eigenvectorsData}
                columns={eigenvectorColumns}
                pagination={false}
                bordered
                size="middle"
              />
            </div>

            <div>
              <Title level={5}>Characteristic:</Title>
              <ul className="list-disc list-inside space-y-1">
                <li>
                  Matrix dimension: {results.eigenvalues.eigenvectors.length} × {results.eigenvalues.eigenvectors[0].length}
                </li>
                <li>
                  Number of eigenvalues: {results.eigenvalues.eigenvalues.length}
                </li>
              </ul>
            </div>
          </div>
        </Card>
      )}
    </div>
  );
};