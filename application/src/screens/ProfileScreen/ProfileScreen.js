import React from "react";
import { Form, Button, Row, Col } from "react-bootstrap";
import "./ProfileScreen.css";
import Balance from '../../components/Balance'
import TransactionList from '../../components/TransactionList'
import AddTransaction from '../../components/AddTransaction'
import { GlobalProvider } from '../../Reducers/GlobalState';
import CardForm from "../../components/Card";

const ProfileScreen = ({ location, history }) => {
   
    return (
            <div>
            <h2> Welcome User </h2>
                <Row className="profileContainer">
                    <Col md={6}>
                        <Form >
                            <Form.Group controlId="email">
                                <Form.Label>Email Address</Form.Label>
                                <Form.Control
                                    type="email"
                                    placeholder="Enter Email"
                                    
                                ></Form.Control>
                            </Form.Group>
                            <Form.Group controlId="password">
                                <Form.Label>Password</Form.Label>
                                <Form.Control
                                    type="password"
                                    placeholder="Enter Password"
                                    
                                ></Form.Control>
                            </Form.Group>
                            <Form.Group controlId="confirmPassword">
                                <Form.Label>Confirm Password</Form.Label>
                                <Form.Control
                                    type="password"
                                    placeholder="Confirm Password"
                                ></Form.Control>
                            </Form.Group>{" "}
                            
                            <Button type="submit" varient="primary">
                                Update
                            </Button>
                        </Form>
                    <GlobalProvider>
                        <div className="container">
                            <Balance />
                            <TransactionList />
                            <AddTransaction />
                        </div>
                    </GlobalProvider>
                    </Col>
                    <Col
                        style={{
                            display: "flex",
                            alignItems: "center",
                            justifyContent: "center",
                        }}
                    >
                    </Col>
                </Row>
            </div>
    );
};

export default ProfileScreen;