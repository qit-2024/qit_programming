// src/App.tsx
import React from 'react';
import { Tabs, Layout } from 'antd';
import { EigenvaluesTab } from './components/operations/EigenValuesTab/EigenvaluesTab';
import { DeterminantTab } from './components/operations/DeterminantTab';
import { PropertiesTab } from './components/operations/PropertiesTab';
import { TensorProductTab } from './components/operations/TensorProductTab';
import { DensityMatrixTab } from './components/quantum/DensityMatrixTab';
import './App.scss';

const { Content, Header } = Layout;
const { TabPane } = Tabs;

const App: React.FC = () => {
  return (
    <Layout className="min-h-screen">
      <Header className="bg-white header">
        <h1 className="text-2xl title">Matrix calculator</h1>
      </Header>
      
      <Content className="p-6">
        <Tabs defaultActiveKey="1" type="card">
          <TabPane tab="Eigenvalues and eigenvector" key="1">
            <EigenvaluesTab />
          </TabPane>
          
          <TabPane tab="Determinant" key="2">
            <DeterminantTab />
          </TabPane>
          
          <TabPane tab="Matrix properties" key="3">
            <PropertiesTab />
          </TabPane>
          
          <TabPane tab="Tensor product" key="4">
            <TensorProductTab />
          </TabPane>
          <TabPane tab="Density matrix of Quantum State" key="5">
            <DensityMatrixTab />
          </TabPane>
        </Tabs>
      </Content>
    </Layout>
  );
};

export default App;
