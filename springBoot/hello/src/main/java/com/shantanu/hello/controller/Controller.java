package com.shantanu.hello.controller;


import com.shantanu.hello.model.HelloMessage;
import com.shantanu.hello.service.HelloService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class Controller {

    @Autowired
    HelloService helloService;

    @RequestMapping(value = "/hello")
    public HelloMessage hello() {
        return  helloService.getHello();
    }


}
