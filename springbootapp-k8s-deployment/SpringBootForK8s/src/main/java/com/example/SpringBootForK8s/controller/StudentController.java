package com.example.SpringBootForK8s.controller;

import com.example.SpringBootForK8s.model.Student;
import com.example.SpringBootForK8s.service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;


    @CrossOrigin(origins = "http://34.31.148.248", allowCredentials = "true")
    @RestController
    public class StudentController {

        @Autowired
        private StudentService service;
        @GetMapping("all")
        public List<Student> allStudents(){

            return service.getAllStudents();
        }

        @PostMapping("add")

        public String saveStudent(@RequestBody Student student){
            service.saveStudent(student);
            return "Saved";
        }

        @GetMapping("/viewStudent")

        public String viewStudent(){
            return "Hello There v2";
        }
}
