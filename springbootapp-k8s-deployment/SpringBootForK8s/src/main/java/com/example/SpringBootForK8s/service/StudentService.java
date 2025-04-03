package com.example.SpringBootForK8s.service;


import com.example.SpringBootForK8s.dao.StudentRepo;
import com.example.SpringBootForK8s.model.Student;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class StudentService {

    @Autowired
    private StudentRepo repo;

    public List<Student> getAllStudents(){
        return repo.findAll();
    }
    public void saveStudent(Student student){
        repo.save(student);
    }
}