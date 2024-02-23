"use client";

import React, { useEffect, useRef, useState } from "react";
import {
  Box,
  Center,
  Heading,
  VStack,
  Button,
  Image,
  Text,
  Flex,
  Link,
  Spacer,
  FormControl,
  FormLabel,
  Textarea,
  SlideFade,
  IconButton,
  Skeleton,
} from "@chakra-ui/react";
import { DownloadIcon } from "@chakra-ui/icons";
import Navbar from "@/components/navbar";

export default function AbstractGenerationPage() {
  const [text, setText] = useState("");
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = () => {
    setSubmitted(true);
  };

  const [imageGenerated, setImageGenerated] = useState(false);
  const [generatedImageUrl, setGeneratedImageUrl] = useState("");

  const [isLoading, setIsLoading] = useState(false);

  const handleGenerateClick = () => {
    setImageGenerated(false);
    setIsLoading(true);
    setTimeout(() => {
      const url = "graph.png";
      setGeneratedImageUrl(url);
      setImageGenerated(true);
      setIsLoading(false);
    }, 5000);
  };

  let handleInputChange = (e: { target: { value: any; }; }) => {
    let inputValue = e.target.value
    setText(inputValue)
  }

  const videoBlurStyle = `
  .background-video {
    -webkit-filter: blur(8px); /* Chrome, Safari, Opera */
    filter: blur(8px); /* Standard syntax */
  }
`;
  const videoRef = useRef<HTMLVideoElement>(null);

  // useEffect(() => {
  //   if (videoRef.current) {
  //     videoRef.current.playbackRate = 0.7;
  //   }
  // }, []);

  return (
    <Box>
      <Navbar />

      <Box height="100vh" px={"3vw"} color="black">
        <>
          <style>{videoBlurStyle}</style>
          <Box
            as="video"
            autoPlay
            loop
            muted
            playsInline
            position="absolute"
            zIndex="-1"
            top="0"
            left="0"
            backdropBlur={8}
            // filter="auto"
            // blur="4px"
            ref={videoRef}
          >
            <source src="/background3.mp4" type="video/mp4" />
            Your browser does not support the video tag.
          </Box>
        </>
        <Box
          position="fixed"
          top="0"
          left="0"
          width="100vw"
          height="100vh"
          zIndex="-1"
          bgGradient="linear(to-tr, brand.100, brand.300)"
          opacity="0.5"
        ></Box>
        <Flex h={"full"} alignItems={"center"} justifyContent={"center"} px="5">
          <VStack
            boxShadow="dark-lg"
            borderRadius={"20px"}
            p="10"
            alignItems={"left"}
            justifyContent={"center"}
            spacing={5}
            width={"35vw"}
            backdropFilter={"blur(8px) brightness(150%)"}
          >
            <Text
              lineHeight="55px"
              fontSize="5xl"
              fontWeight="semi-bold"
              align={"left"}
              color="white"
            >
              Abstract Generation
            </Text>
            <Text fontSize="large" align={"left"} color="white">
            SciSketch can automatically analyze the content of life science papers and generate informative and visually appealing graphical abstracts. This tool will significantly reduce the time and effort required to create graphical abstracts and enhance the accessibility and understanding of scientific literature.
            </Text>
          </VStack>

          <Spacer />

          <VStack
            boxShadow="dark-lg"
            spacing={4}
            //align="stretch"
            mt={4}
            width="50vw"
            backdropFilter={"blur(8px) brightness(150%)"}
            borderRadius={"20px"}
            px="5"
            pt="5"
          >
            <Textarea
              placeholder="Enter your text here..."
              size="md"
              background={"white"}
              height={"20vh"}
              value={text}
              onChange={handleInputChange}
            />
            <Button
              color="white"
              boxShadow="dark-lg"
              bg="brand.200"
              _hover={{
                color: "gray",
                bgGradient: "linear(to-tr, brand.100, brand.300)",
              }}
              onClick={handleGenerateClick}
              size="lg"
              isLoading={isLoading}
              loadingText="Generating..."
              disabled={isLoading}
            >
              Generate
            </Button>
            <Box position="relative">
              {imageGenerated && (
                // <Skeleton
                //   my="4"
                //   startColor="brand.500"
                //   endColor="brand.100"
                //   height="40vh"
                //   borderRadius={"10"}
                // ></Skeleton>
                <Image
                  src={generatedImageUrl}
                  alt="Generated Image"
                  borderRadius={"10"}
                  boxShadow="dark-lg"
                  width="800px"
                  //height="40vh"
                  my="4" />
              )}
            </Box>
          </VStack>
        </Flex>
      </Box>
    </Box>
  );
}
