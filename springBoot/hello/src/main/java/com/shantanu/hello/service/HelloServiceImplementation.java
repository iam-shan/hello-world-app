package com.shantanu.hello.service;



import com.shantanu.hello.model.HelloMessage;
import org.springframework.stereotype.Service;



@Service
public class HelloServiceImplementation implements HelloService {

    @Override
    public HelloMessage getHello() {
        return new HelloMessage("Hello");
    }
}
