package com.example.SpringBootForK8s.dao;

import com.example.SpringBootForK8s.model.Student;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface StudentRepo extends JpaRepository<Student,Integer> {


}

